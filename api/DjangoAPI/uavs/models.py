from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from dealer.models import *
# Create your models here.

class UAVs(models.Model):
    Id = models.AutoField(primary_key=True)
    Model = models.CharField(max_length=500)
    Brand = models.CharField(max_length=500)
    Weight = models.CharField(max_length=500)
    Category = models.CharField(max_length=500)
    Dealer = models.ForeignKey(Dealers, on_delete=models.PROTECT)
    Area = models.ForeignKey(Area, on_delete=models.SET_NULL, null = True)
    is_available = models.BooleanField(default = True)
