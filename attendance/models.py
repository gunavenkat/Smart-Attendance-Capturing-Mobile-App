from django.db import models

# Create your models here.
# models.py
class User(models.Model):
    pic= models.ImageField(upload_to="user_uploaded",default='')

class Image(models.Model):
    username = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')