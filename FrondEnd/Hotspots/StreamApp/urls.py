from django.urls import path
from django.urls import include, re_path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.results),
    path('<str:state_name>weather', views.state_weather)
]