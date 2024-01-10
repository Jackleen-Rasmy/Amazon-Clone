from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from .choices import ORDER_TYPE
from django.utils import timezone
from utils.generate_code import generate_code
from accounts.models import Address
from products.models import Product
import datetime

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_owner', on_delete=models.SET_NULL ,blank=True,null=True)
    status = models.CharField(max_length=20,choices=ORDER_TYPE)
    code = models.CharField(max_length=10, default=generate_code)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(blank=True,null=True)
    delivery_address = models.ForeignKey(Address, related_name='delivery_address',on_delete=models.SET_NULL, blank=True,null=True)
    coupon = models.ForeignKey('Coupon', related_name='order_coupon', on_delete=models.SET_NULL, null=True,blank=True)
    total = models.FloatField()
    total_with_coupon = models.FloatField(blank=True,null=True)
    

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product , related_name='orderdetail_product', on_delete=models.SET_NULL, blank=True,null=True)
    quatity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    
    
class Coupon(models.Model):
    code = models.CharField(max_length=20)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    quantity = models.IntegerField()
    discount = models.FloatField()
    
    def save(self, *args, **kwargs):
        week = datetime.timedelta(days=7)
        self.end_date = self.start_date + week
        super(Coupon, self).save(*args, **kwargs)
        
    
