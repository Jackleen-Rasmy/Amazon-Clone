from rest_framework import serializers
from .models import Product, Brand, ProductImages, Review

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
        
class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.IntegerField()
    avg_rate = serializers.FloatField()
    # review_count = serializers.SerializerMethodField()
    # avg_rate = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
        
    # def get_review_count(self,object):
    #     # reviews = object.review_product.all().count()
    #     reviews = object.review_count()
    #     return reviews
    
    # def get_avg_rate(self,object):
    #     avg = object.avg_rate()
    #     return avg
        # total = 0
        # reviews = object.review_product.all()
        # if len(reviews) > 0:
        #     for item in reviews:
        #         total += int(item.rate)
            
        #     avg = total / len(reviews)
            
        # else:
        #     avg = 0
            
        # return avg
    
        
class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.IntegerField()
    avg_rate = serializers.FloatField()
    # review_count = serializers.SerializerMethodField()
    # avg_rate = serializers.SerializerMethodField()
    images = ProductImagesSerializer(source='product_image',many=True)
    reviews = ReviewSerializer(source='review_product',many=True)
    
    class Meta:
        model = Product
        fields = '__all__'

    # def get_review_count(self,object):
    #     reviews = object.review_product.all().count()
    #     return reviews
    
    # def get_avg_rate(self,object):
    #     total = 0
    #     reviews = object.review_product.all()
    #     if len(reviews) > 0:
    #         for item in reviews:
    #             total += int(item.rate)
            
    #         avg = total / len(reviews)
            
    #     else:
    #         avg = 0
            
    #     return avg
    
          
class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'         