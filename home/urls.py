from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("contact/tryy",views.tryy,name='tryy'),
    path("services/mobile",views.mobile,name='mobile'),
    path("services/laptop",views.laptop,name='laptop'),
    path("services/something",views.something,name='something')   
]