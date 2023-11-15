from django.contrib import admin
from django.urls import path

from .views import home,registrar,login

urlpatterns = [
    path('',home,name="inicio"),
    path('registrar',registrar,name="registrar"),
    path('login',login,name="login")
]