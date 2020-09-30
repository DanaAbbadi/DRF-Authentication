from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Weather(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    region      = models.CharField(max_length=64)
    country      = models.CharField(max_length=64)
    status   = models.CharField(max_length=64)
    date    = models.CharField(max_length=64)

    def __str__(self):
        return self.country