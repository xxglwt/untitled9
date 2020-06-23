"""untitled9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# # from django.urls import path
# #
# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# # ]

from django.conf.urls import url, include
from . import view
from TestModel import search
from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    # url(r'^$',view.hello),
    # url('hello/',view.hello),
    # url('name/',view.getname),
    # url('shuchu',view.output),
    # url('add',view.testdb),
    url('show', view.show),
    # url(r'^search$',view.search),
    # url(r'^search_form$',view.search_form),
    url('addname_form/', view.addname_form),
    url('addname/', view.addname),
    url('search-form', view.searchform),
    url('search', view.search),
    url(r'^admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('demo/', include('demo.urls')),

    path('index/', views.index),
    path('login/',views.login),
    path('captcha/', include('captcha.urls')),
    path('logout/' , views.logout),
    path('register/', views.register),

]
