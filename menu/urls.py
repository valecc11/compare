from django.contrib import admin
from django.urls import path

from .views import home,registrar,login

urlpatterns = [
    path('inicio',home,name="inicio"),
    path('',registrar,name="registrar"),
    path('login',login,name="login")
]