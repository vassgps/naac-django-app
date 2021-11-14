from django.shortcuts import render
from django.http import HttpResponse


# Home Page of the Website
def index(request):
    return render(request, 'proApp/index.html')

def login(request):
    return render(request, 'proApp/login.html')

def register(request):
    return render(request, 'proApp/register.html')