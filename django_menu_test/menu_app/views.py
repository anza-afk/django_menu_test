from django.shortcuts import render

# Create your views here.
def index(request, pk=None):
    context = {}
    return render(request, 'menu_app/test.html', context)