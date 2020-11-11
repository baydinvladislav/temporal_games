from django.shortcuts import render
from .models import Solution

def index(request):
    return render(request, "main/index.html")

def core_engineer(request):
    return render(request, "main/core_engineer.html")

def vfx_artist(request):
    return render(request, "main/vfx_artist.html")

def ui_designer(request):
    return render(request, "main/ui_designer.html")

def data_scientist(request):
    return render(request, "main/data_scientist.html")
