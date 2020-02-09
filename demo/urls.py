# author
# -*- coding:utf-8 -*-
# create time 2019年12月27日 14:25
from django.urls import path
from . import views

app_name='demo'
urlpatterns=[
    path('index',views.index),
]