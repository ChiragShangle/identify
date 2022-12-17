from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checking),
    path('identify', views.identify_people)
    
]


