from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
path('',views.HomePage,name='HomePage'),
path('Destination/',views.DestinationPage,name='Destination'),
path('Test/',views.get_name,name='getname'),
path('your_name/',views.get_name,name='getname'),
path('contact/',views.send_email,name='contact'),
path('Home/PackagesRest/',views.packages_collection),
]
