from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("team",views.team,name='team'),
    path("gallery",views.gallery,name='gallery'),
    path("lifetime",views.lifetime,name='lifetime'),
    path("distributor",views.distributor,name='distributor'),
    path("contact",views.contact,name='contact'),
    path("register",views.register,name='register'),





]
