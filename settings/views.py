from django.shortcuts import render
from products.models import Product, Review, Brand
from django.db.models import Count



def home(request):
    new_products = Product.objects.filter(flag='New')[:10]
    sale_products = Product.objects.filter(flag='Sale')[:10]
    featured_products = Product.objects.filter(flag='Feature')[:6]
    brands =  Brand.objects.annotate(product_count=Count('product_brand'))[:10]
    reviews = Review.objects.all()
    
    
    return render(request,'settings/home.html',{
        
        'new_products':new_products,
        'sale_products':sale_products,
        'featured_products':featured_products,
        'brands':brands,
        'reviews':reviews
        
    })
