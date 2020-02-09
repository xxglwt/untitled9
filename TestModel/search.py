# author
# -*- coding:utf-8 -*-
# create time 2019年12月01日 8:06
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpRequest

def search_form(request):
    return  render_to_response("search_form.html")

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message="你搜索的内容是："+request.GET['q']
    else:
        message="你提交了空表单"
    return HttpResponse(message)


