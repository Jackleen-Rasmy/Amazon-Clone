from django.db import models
from django.contrib.auth.models import User
from .choices import ADDRESS_TYPE


class Address(models.Model):
    user = models.ForeignKey(User , related_name='user_address', on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    type = models.CharField(max_length=12,choices=ADDRESS_TYPE)

    
    
class DeliveryFee(models.Model):
    fee = models.IntegerField()
    
 
    
