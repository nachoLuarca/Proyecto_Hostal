from django.shortcuts import render
from .models import Projecto


def Portfolio(request):
    projects = Projecto.objects.all()
    return render(request,"Hostal/Portafolio.html",{'projects':projects})
   
# Create your views here.
