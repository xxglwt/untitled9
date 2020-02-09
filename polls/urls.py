# author
# -*- coding:utf-8 -*-
# create time 2019年12月06日 22:16

from django.urls import path
from . import views

app_name='poll'
urlpatterns=[
    path('',views.index,name='index2'),
    path('<int:pk>/detail/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    # path('<int:question_id>/detail/',views.detail,name='detail'),
    path('<int:question_id>/vot/',views.vote,name='vote'),
    # path('<int:question_id>/results/',views.results,name='results'),


]