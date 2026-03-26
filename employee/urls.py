from django.urls import path
from . import views

urlpatterns = [
    #path('route',view)
    path('', views.home),
    path('home',views.home),
    path('contact',views.contact),
    path('about',views.about),
    path('emplist',views.emplist)
]