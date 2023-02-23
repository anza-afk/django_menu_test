from django import template
from menu_app.models import MenuItem
from menu_app.utils import get_current_url, get_acive_item



register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.inclusion_tag('menu_app/menu_template.html', takes_context=True)
def draw_menu(context, name):

    if 'menu_query' in context:
        menu_query = context['menu_query']
        current_item = menu_query.filter(name=name).first()
    else:
        menu_query = MenuItem.objects.select_related('menu').all()
        current_item = None
    if not current_item:
        current_item = menu_query.filter(parent=None).first()


    current_url = get_current_url(context)
    active_item = get_acive_item(menu_query, current_url)

    print(current_url)
    print(active_item)

    if 'active' in context:
        active = context['active']
    else:
  
        active = MenuItem.get_parents(active_item)
        print(MenuItem.get_parents(active_item))
        active.append(active_item.id)
    
    children = {}
    children[current_item.id] = [item for item in menu_query if item.parent == current_item]

    print(active)
    return {
        'menu_item': current_item,
        'children': children,
        'active': active,
        'menu_query': menu_query
    }




# @register.inclusion_tag('menu_app/menu_template.html', takes_context=True)
# def draw_menu(context, name):

#     menu_query = MenuItem.objects.select_related('menu').filter(menu__name=name)
#     menu_items = list(menu_query.filter(parent=None))

#     try:
#         current_url = context['request'].path
#     except KeyError:
#         current_url = '/'

#     current_item = menu_query.filter(url=current_url).first()

#     active = [current_item.id]

#     children = {menu_item.id : [item for item in menu_query if item.parent == menu_item] for menu_item in menu_items}

#     return {
#         'menu': menu_query,
#         'menu_items': menu_items,
#         'menu_item': current_item,
#         'children': children,
#         'active': active,
#     }




@register.inclusion_tag('menu_app/menu_template.html', takes_context=True)
def draw_menu___(context, name):

    if 'menu_query' in context:

        menu_query = context['menu_query']
        current_item = menu_query.filter(name=name).first()
        # print(name, current_item)
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


    if 'children' in context:
        children = context['children']
    else:
        children = {}
    # children = [item for item in menu_query if item.parent == current_item]
    children[current_item.id] = [item for item in menu_query if item.parent == current_item]
    print('FATH', current_item, 'CH', children)
    return {
        'menu_item': current_item,
        'children': children,
        'active': active,
        'menu_query': menu_query
    }

