from django import template
from menu_app.models import MenuItem
from menu_app.utils import get_current_url, get_acive_item, get_url_path

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.inclusion_tag(
    'menu_app/menu_templates/menu_template.html',
    takes_context=True
)
def draw_menu(context, name):

    if 'menu_query' in context:
        menu_query = context['menu_query']
        current_item = next(filter(
            lambda item: item['name'] == name, menu_query
        ))

    else:
        _query = MenuItem.objects.select_related('menu').all()
        menu_query = [menu_item.__dict__ for menu_item in _query]

        current_item = None

    if not current_item:
        current_item = next(
            filter(lambda item: item['parent_id'] is None, menu_query)
        )

    current_url = get_current_url(context)
    active_item = get_acive_item(menu_query, current_url)

    menu_item = {
        'id': current_item['id'],
        'name': current_item['name'],
        'url': get_url_path(current_item),
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
