from django.shortcuts import render

# Create your views here.

def index(request,a,b):
    result = a+b
    return render(request,"addition/index.html",{'result':result})

