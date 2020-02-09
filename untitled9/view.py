# author
# -*- coding:utf-8 -*-
# create time 2019年11月16日 6:51

from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test
from django.shortcuts import render_to_response

def hello(request):
    # return HttpResponse("hello world")
    context={}
    context['hello']='hello world'
    return render(request,'hello.html',context)

def getname(request):
    content={}
    content['abc']="wangtie"
    return render(request,'getname.html',content)

def output(request):
    return HttpResponse("<h1>中华人民共和国</h1>")

def testdb(request):
    test1=Test(name="liming")
    test1.save()
    test2=Test(name="张吉媛")
    test2.save()
    return HttpResponse("<p>数据添加成功")

def show(request):
    test1=Test.objects.all()
    response1=""
    for var in test1:
        response1+=var.name+"  "
    return HttpResponse("<p>"+response1+"</p>")



def search_form(request):
    return  render_to_response("search_form.html")

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message="你搜索的内容是："+request.GET['q']
    else:
        message="你提交了空表单"
    return HttpResponse(message)

def addname_form(request):
    return render(request,"nameadd.html")

def addname(request):
    request.encoding="utf-8"
    namevalue=request.GET['content']
    test1=Test(name=namevalue)
    test1.save()
    return HttpResponse("添加成功了")

def searchform(request):
    request.encoding="utf-8"
    return render_to_response("search-form.html")

def search(request):
    request.encoding="utf-8"
    id=request.POST["id"]
    aa=Test.objects.get(id=id)
    result={}
    result['id']=aa.name
    return render(request,"search-form.html",result)


