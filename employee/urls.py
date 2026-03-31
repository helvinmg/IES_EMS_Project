from django.urls import path
from . import views

urlpatterns = [
    #path('route',view)
    path('', views.home),
    path('home',views.home),
    path('contact',views.contact),
    path('about',views.about),
    path('emplist',views.emplist,name="emplist"),
    path('managerlist',views.managerlist),
    path('delete/<int:id>',views.empdelete),
    path('emp/add',views.empcreate)
    #dynamic route which recceives id of emp
]