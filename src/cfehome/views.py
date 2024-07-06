from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request,*args,**kwargs):
    template = "home.html"
    context = {
        "title":'Home Page'
    }
    return render(request,template_name=template,context=context)