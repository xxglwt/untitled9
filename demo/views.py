from django.shortcuts import render
from django.http import *
# Create your views here.

def index(request):
    a={}
    a["item"]="中华人民共和国"
    a["personname"]="wang tie"
    a["list"]={'a','b','c','d'}
    return render(request,"demo/index.html",a)