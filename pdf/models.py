from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    previous_work = RichTextField(null=True,blank=True)
    skills = RichTextField(null=True,blank=True)
    projects = RichTextField(null=True,blank=True)
