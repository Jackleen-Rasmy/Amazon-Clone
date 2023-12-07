from django.db import models
from .choices import FLAG_TYPES
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(_('name'),max_length=255)
    flag = models.CharField(_('flag'),max_length=255,choices=FLAG_TYPES)
    price = models.FloatField(_('price'))
    image = models.ImageField(_('image'),upload_to='product')
    sku = models.IntegerField(_('sku'))
    tags = TaggableManager()
    subtitle = models.TextField(_('subtitle'),max_length=500)
    description = models.TextField(_('description'),max_length=50000)
    brand = models.ForeignKey('Brand', related_name='product_brand',verbose_name=_('brand'),on_delete=models.SET_NULL, null=True)
    
    slug = models.SlugField(blank=True,null=True, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
        
    


class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_image',verbose_name=_('product'), on_delete=models.CASCADE)
    image = models.ImageField(_('image'),upload_to='product_images')
    

class Brand(models.Model):
    name = models.CharField(_('name'),max_length=255)
    image = models.ImageField(_('image'),upload_to='brand')
    slug = models.SlugField(blank=True,null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)     

    def __str__(self):
        return self.name   
    
class Review(models.Model):
    user = models.ForeignKey(User, related_name='review_user',verbose_name=_('user'), on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name='review_product',verbose_name=_('product'), on_delete=models.CASCADE)
    review = models.TextField(_('review'),max_length=10000)
    rate = models.CharField(_('rate'),max_length=100, choices=[(i,i) for i in range(1,6)])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.rate}"