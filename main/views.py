from django.shortcuts import render
from .models import Solution, Job
from django.views import generic

def index(request):
    solutions = Solution.objects.all()
    jobs = Job.objects.all()
    return render(request, "main/index.html", {'solutions': solutions, 'jobs': jobs})

def core_engineer(request):
    jobs = Job.objects.all()
    return render(request, "main/core_engineer.html", {'jobs': jobs})

def vfx_artist(request):
    jobs = Job.objects.all()
    return render(request, "main/vfx_artist.html", {'jobs': jobs})

def ui_designer(request):
    jobs = Job.objects.all()
    return render(request, "main/ui_designer.html", {'jobs': jobs})

def data_scientist(request):
    jobs = Job.objects.all()
    return render(request, "main/data_scientist.html", {'jobs': jobs})

def riflecore(request):
    jobs = Job.objects.all()
    return render(request, "main/riflecore.html", {'jobs': jobs})
