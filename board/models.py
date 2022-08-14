from django.db import models

# Create your models here.
class Auth(models.Model):
    userId = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True, blank=True)

class Test(models.Model):
    id = models.IntegerField(primary_key=True)