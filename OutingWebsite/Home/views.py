from django.shortcuts import render
from Home.models import Packages
from .forms import NameForm
from .forms import ContactForm
from django.http import HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Home.serializers import PackagesSerializer
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'Thanks.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'Test.html', {'form': form})
def contact_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:   
        if form.is_valid():
           subject = form.cleaned_data['subject']
           message = form.cleaned_data['message']
           sender = form.cleaned_data['sender']
           cc_myself = form.cleaned_data['cc_myself']

           recipients = ['sanjaynandy89@gmail.com']
           if cc_myself:
              recipients.append(sender)
           send_mail(subject, message, sender, recipients)
           return render(request, 'Thanks.html')
    else:
        form = ContactForm()       
    return render(request, 'ContactForm.html', {'form': form})
def HomePage(request):
     pkgs=Packages.objects.all()
     return render(request,'Home.html',{'pkgs':pkgs})
def DestinationPage(request):
     return render(request,'Bhutan.html')     

