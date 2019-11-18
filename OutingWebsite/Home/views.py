from django.shortcuts import render
from .models import Packages
from .forms import NameForm
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import BadHeaderError,send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PackagesSerializer
from django.core.mail import EmailMessage
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
def send_email(request):
      if request.method == 'POST':
        # create a form instance and populate it with data from the request:
           form = ContactForm(request.POST)
        # check whether it's valid:  
           if form.is_valid(): 
                subject = request.POST.get('subject', '')
                message = request.POST.get('message', '')
                from_email = request.POST.get('sender', '')
                if subject and message and from_email:
                         try:
                               send_mail(subject, message, from_email, ['pallab.mukherjee73@gmail.com'])
                         except BadHeaderError:
                               return HttpResponseRedirect('Invalid header found.')
                         return render(request, 'Thanks.html')
      else:
          form = ContactForm()       
      return render(request, 'ContactForm.html', {'form': form})       
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
           phoneno = form.cleaned_data['phoneno']
           cc_myself = form.cleaned_data['cc_myself']

           recipients = ['sanjaynandy89@gmail.com']
           if cc_myself:
              recipients.append(sender)
           email = EmailMessage(subject,message,sender,recipients,headers={'Message-ID': 'foo'},)
           email.send()
           return render(request, 'Thanks.html')
    else:
        form = ContactForm()       
    return render(request, 'ContactForm.html', {'form': form})
def HomePage(request):
     pkgs=Packages.objects.all()
     form=ContactForm(request.POST)
     return render(request,'Home.html',{'pkgs':pkgs})
def DestinationPage(request):
     return render(request,'Bhutan.html')     
def packages_collection(self,request):
    if request.method == 'GET':
        Pkgs1 = Packages.objects.all()
        serializer = PackagesSerializer(Pkgs1, many=True)
        return Response(serializer.data)
