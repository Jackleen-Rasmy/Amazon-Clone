from django.db import models
from django.contrib.auth.models import User
from .choices import ADDRESS_TYPE, PHONE_TYPE
from utils.generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver



class Address(models.Model):
    user = models.ForeignKey(User , related_name='user_address', on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    type = models.CharField(max_length=12,choices=ADDRESS_TYPE)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile')
    code = models.CharField(max_length=10,default=generate_code)
    
    def __str__(self):
        return str(self.user)
    
@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )
        
    
    
    
class ContactNumbers(models.Model):
    user = models.ForeignKey(User, related_name="user_contact", on_delete=models.CASCADE)  
    type = models.CharField(max_length=10, choices=PHONE_TYPE)
    number = models.CharField(max_length=25)
    



    



    
    

    
 
    
