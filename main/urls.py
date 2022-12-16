from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checking),
    path('test', views.test),
    path('identify', views.identify_people)
    
]


