from django.contrib import admin
from django.urls import path
from book.views import *
urlpatterns = [
    path('index/', index),
    path('<city_id>/<shop_id>', shop),
    path('register/', register),
    path('json/', json_learn),
]