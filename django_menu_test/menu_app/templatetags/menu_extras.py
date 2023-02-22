from django import template
from django.urls import reverse
from menu_app.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu_app/menu_template.html', takes_context=True)
def draw_menu(context, name, parent = None):
    if parent:
        menu = context['menu']

        menu = MenuItem.objects.get(name=name)
    else:
        menu_query = MenuItem.objects.select_related('menu').all()
        # menu = Menu.objects.select_related('parent').all()
        
        try:
            current_url = context['request'].path
        except KeyError:
            current_url = '/'
        current_menu_item = menu_query.filter(url=current_url).first()
        menu = []

        for item in menu_query:
            if 'http' in item.url:
                url = item.url
            else:
                url = reverse(item.url)

            menu.append({
                'item':  item
            })
        #     print(item)
        #     local_context.append(item)

    return {
        'menu': menu,

        # 'current_menu_item': current_menu_item,
        # 'active': active,
    }