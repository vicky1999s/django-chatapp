from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "asgichatapp/index.html")

def home(request):
    return render(request, "asgichatapp/home.html")