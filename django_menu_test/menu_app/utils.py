from django.urls import resolve, reverse, NoReverseMatch
from django.template.context import RequestContext


def filter_list(menu_query: list, key: str, filter: str) -> dict:
    """Filters list of dicts and returns one item (first)."""
    for item in menu_query:
        if item[key] == filter:
            return item


def get_current_url(context: RequestContext) -> str:
    """Returns current url."""
    try:
        current_url = context['request'].path
    except KeyError:
        current_url = '/'
    return current_url


def get_acive_item(menu_query: list[dict], current_url: str) -> dict:
    """Returns active item in menu."""
    active_item = filter_list(menu_query, 'url', resolve(current_url).url_name)
    if not active_item:
        active_item = filter_list(menu_query, 'url', current_url)
    print(current_url, active_item)
    return active_item


def get_url_path(item: dict) -> str:
    """Returns url path. Reversed from named url if possible."""
    try:
        url_path = reverse(item['url'])
    except NoReverseMatch:
        url_path = item['url']
    return url_path
