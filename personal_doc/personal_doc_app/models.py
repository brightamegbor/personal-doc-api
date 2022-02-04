from django.db import models

# Create your models here.
class Users(models.Model):
  username = models.CharField(max_length=80, blank=False, default='', unique=True)
  password = models.CharField(max_length=30, blank=False, default='')
