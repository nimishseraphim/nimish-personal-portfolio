from django.shortcuts import render
from .models import Project


# Create your views here.

def home(request):
    projects = Project.objects.all()  # grab all objects from Projects model
    return render(request, 'portfolio/home.html', {'projects': projects})
