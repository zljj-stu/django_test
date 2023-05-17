from django.contrib import admin
from django.urls import path
from book.views import index, shop
urlpatterns = [
    path('index/', index),
    path('<city_id>/<shop_id>', shop),
]