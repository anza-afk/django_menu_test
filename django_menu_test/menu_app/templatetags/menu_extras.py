from django import template
from menu_app.models import MenuItem
from menu_app import utils
from django.template.context import RequestContext
register = template.Library()


@register.filter
def get_item(dictionary: dict, key: str) -> dict:
    """Filter for getting item from diict by any key in template"""
    return dictionary.get(key)


@register.inclusion_tag(
    'menu_app/menu_templates/menu_template.html',
    takes_context=True
)
def draw_menu(context: RequestContext, name: str) -> dict:
    """Template tag menu logic"""
    if 'menu_query' in context:
        menu_query = context['menu_query']
        current_item = utils.filter_list(menu_query, 'name', name)
    else:

        _query = MenuItem.objects.select_related('menu').filter(menu__name=name)
        menu_query = [menu_item.__dict__ for menu_item in _query]

        current_item = None

    if not current_item:
        current_item = utils.filter_list(menu_query, 'parent_id', None)

    current_url = utils.get_current_url(context)

    active_item = utils.get_acive_item(menu_query, current_url)

    menu_item = {
        'id': current_item['id'],
        'name': current_item['name'],
        'url': utils.get_url_path(current_item),
    }

    if 'active' in context:
        active = context['active']
    else:
        active = MenuItem.get_parents(active_item, menu_query)
        active.append(active_item['id'])

    children = {}
    children[current_item['id']] = list(filter(
        lambda item: item['parent_id'] == current_item['id'], menu_query
    ))

    return {
        'menu_item': menu_item,
        'children': children,
        'active': active,
        'menu_query': menu_query
    }
