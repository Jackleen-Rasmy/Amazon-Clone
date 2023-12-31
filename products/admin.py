from django.contrib import admin
from .models import Product, ProductImages, Brand, Review


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    search_fields = ['name']
    list_display = ['name', 'avg_rate', 'review_count']
    



admin.site.register(Product , ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)

