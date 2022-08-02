from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.CharField(max_length=255, null=True)
    image_url = models.ImageField(upload_to="", null=True)
  