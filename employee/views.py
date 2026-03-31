from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Manager
from .forms import EmployeeForm
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

def empdelete(request,id):
    print("deleteing ",id)
    record=Employee.objects.get(id=id)
    record.delete()
    return redirect("emplist")

def empcreate(request):
    if request.method=="GET":#first time when emp/add is called
        form=EmployeeForm()
        return render(request,'empcreate.html',{'form':form})
    else:#when form is submitted
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()#insert into employee
            return redirect("emplist")
        else:
            return render(request,'empcreate.html',{'form':form})
        
def empupdate(request,id):
    if request.method=="GET":
        record=Employee.objects.get(id=id)
        form=EmployeeForm(instance=record)
        return render(request,'empupdate.html',{'form':form})
    else:
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("emplist")
        else:
            return render(request,'empupdate.html',{'form':form})
