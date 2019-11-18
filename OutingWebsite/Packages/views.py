from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def SikimPackages(request):
    return render(request,'Packages/Sikim/SikimPackage.html')
def OldSilkRoute(request):
    return render(request,'Packages/Sikim/OldSilkRoute.html')
        
    