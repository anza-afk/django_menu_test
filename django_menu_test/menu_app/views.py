from django.shortcuts import render


def index(request, pk=None):
    context = {}
    return render(request, 'menu_app/index.html', context)


def products(request, pk=None):
    context = {}
    return render(request, 'menu_app/products.html', context)


def it(request, pk=None):
    context = {}
    return render(request, 'menu_app/it.html', context)


def chat_bots(request, pk=None):
    context = {}
    return render(request, 'menu_app/chat_bots.html', context)


def shop(request, pk=None):
    context = {}
    return render(request, 'menu_app/shop.html', context)


def about_us(request, pk=None):
    context = {}
    return render(request, 'menu_app/about_us.html', context)


def contacts(request, pk=None):
    context = {}
    return render(request, 'menu_app/contacts.html', context)


def second_index(request, pk=None):
    context = {}
    return render(request, 'menu_app/second_index.html', context)


def second_shop(request, pk=None):
    context = {}
    return render(request, 'menu_app/second_shop.html', context)