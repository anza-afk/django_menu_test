from django.urls import resolve, reverse, NoReverseMatch


def get_current_url(context):
    try:
        current_url = context['request'].path
    except KeyError:
        current_url = '/'
    return current_url


def get_acive_item(menu_query, current_url):
    active_item = next(filter(
        lambda item: item['url'] == resolve(current_url).url_name, menu_query
    ))
    if not active_item:
        active_item = next(filter(
            lambda item: item['url'] == current_url, menu_query
        ))
    return active_item


def get_url_path(item):
    try:
        url_path = reverse(item['url'])
    except NoReverseMatch:
        url_path = item['url']
    return url_path
