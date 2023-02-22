from django import template
from django.urls import reverse, NoReverseMatch
from menu_app.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu_app/menu_template.html', takes_context=True)
def draw_menu(context, name):

    menu_query = MenuItem.objects.select_related('menu').filter(menu__name=name)
    menu_items = list(menu_query.filter(parent=None))

    try:
        current_url = context['request'].path
    except KeyError:
        current_url = '/'

    current_item = menu_query.filter(url=current_url).first()

    active = [current_item.id]
    children=[]
    for menu_item in menu_items:
        for item in menu_query:
            if item.parent == menu_item:
                children.append(item)
    return {
        'menu': menu_query,
        'menu_items': menu_items,
        'children': children,
        'active': active,
    }

@register.inclusion_tag('menu_app/menu_template.html', takes_context=True)
def draw_menu_item(context, name):

    if 'menu_query' in context:
        menu_query = context['menu_query']
        current_item = menu_query.filter(name=name).first()

    else:
        menu_query = MenuItem.objects.select_related('menu').all()
        current_item = None

    try:
        current_url = context['request'].path
    except KeyError:
        current_url = '/'

    active_item = menu_query.filter(url=current_url).first()

    if not current_item:
        current_item = active_item

    def get_parents(menu_item):
        if menu_item.parent:
            return get_parents(menu_item.parent).append(menu_item.parent.id)
        else:
            return []
    
    active = get_parents(active_item)
    active.append(active_item.id)

    print('active///////')
    print(active)

    children = [item for item in menu_query if item.parent == current_item]

    print('children///////')
    print(children)
    current_item = [current_item]
    return {
        'menu_items': current_item,
        'children': children,
        'active': active,
        'menu_query': menu_query
    }

