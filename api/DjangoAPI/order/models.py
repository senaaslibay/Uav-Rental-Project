from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from dealer.models import *
from uavs.models import *


# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    dealer = models.ForeignKey(Dealers, on_delete=models.PROTECT)
    uav = models.ForeignKey(UAVs, on_delete=models.PROTECT)
    days = models.CharField(max_length = 3)
    is_complete = models.BooleanField(default = False)