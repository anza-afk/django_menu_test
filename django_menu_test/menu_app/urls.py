from django.urls import path
from menu_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='test_page_1'),
    path('it', views.it, name='test_page_1_1'),
    path('chat_bots', views.chat_bots, name='test_page_1_1_1'),
    path('shop', views.shop, name='test_page_2'),
    path('about_us', views.about_us, name='test_page_3'),
    path('contacts', views.contacts, name='test_page_3_1'),
    path('index2', views.second_index, name='second_test_1'),
    path('shop2', views.second_shop, name='second_test_2'),
]
