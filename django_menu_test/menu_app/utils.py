from django.urls import resolve


def get_current_url(context):
    try:
        current_url = context['request'].path
    except KeyError:
        current_url = '/'
    return current_url


def get_acive_item(menu_query, current_url):
    active_item = menu_query.filter(url=resolve(current_url).url_name).first()
    if not active_item:
        active_item = menu_query.filter(url=current_url).first()
    return active_item