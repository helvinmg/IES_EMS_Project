from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def emplist(request):
    #data fetched from db
    records=[{'name':'rahul','salary':56000},{'name':'arjun','salary':45000}]
    return render(request,'empdetails.html',{'records':records,'count':len(records)})
    #context will be in dict format
    #render(request,'templatename',context)
