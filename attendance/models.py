from django.db import models
from .storage import OverwriteStorage
# Create your models here.
# models.py
class User(models.Model):
    pic= models.ImageField(upload_to="user_uploaded",default='',storage=OverwriteStorage())


