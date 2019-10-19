from django.shortcuts import render
from .models import Packages
def HomePage(request):
     pkgs=Packages.objects.all()
     return render(request,'Home.html',{'pkgs':pkgs})
def DestinationPage(request):
     return render(request,'Bhutan.html')     
