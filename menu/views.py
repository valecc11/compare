from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'menu/home.html')

def registrar(request):
    return render(request, 'menu/registrar.html')

def login(request):
    return render(request, 'menu/login.html')

