from django.db import models
# Create your models here.
class Packages(models.Model):
   name = models.CharField('Event Name', max_length=120)
   img=models.ImageField(upload_to='pics')
   description = models.TextField(blank=True)