from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def home_page_view(request,*args,**kwargs):
    return about_view(request,*args,**kwargs)

def about_view(request,*args,**kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = page_qs.count()*100/qs.count()
    except:
        percent=0
    # PageVisit.objects.create()
    template = "home.html"
    context = {
        "title":'Home Page',
        'page_visit_count':percent,
        'total_visit_count':qs.count(),
        'percent':percent,
    }
    PageVisit.objects.create(path=request.path)
    return render(request,template_name=template,context=context)