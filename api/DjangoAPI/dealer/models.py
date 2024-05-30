from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from dealer.models import *
from customer.models import *

# Create your models here.
class Dealers(models.Model):
    dealer = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(13)], max_length = 13)
    area = models.OneToOneField(Area, on_delete=models.PROTECT)
    wallet = models.IntegerField(default = 0)