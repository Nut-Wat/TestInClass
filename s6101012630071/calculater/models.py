from django.conf import settings
from django.db import models

# Create your models here.

class History (models.Model):
    number1=models.IntegerField()
    operater=models.CharField(max_length=255)
    number2=models.IntegerField()
    result = models.IntegerField()

    #def __str__(self):
    #    return self.title