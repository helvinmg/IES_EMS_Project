from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee,Manager
# Create your views here.
def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def emplist(request):
    #data fetched from db
    records=Employee.objects.all()
    #select * from employee
    return render(request,'empdetails.html',{'records':records,'count':len(records)})
    #context will be in dict format
    #render(request,'templatename',context)

def managerlist(request):
    records=Manager.objects.all()
    return render(request,'managerdetails.html',{'records':records})