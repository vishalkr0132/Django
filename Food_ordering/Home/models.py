from django.db import models
from django.contrib.auth.models import User
from msilib.schema import Class

# Create your models here.

class payment(models.Model):
    food = models.CharField(max_length=255, null=True)
    Idno = models.CharField(max_length=255)
    Date = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)

    def __str__(self):
        return self.Idno