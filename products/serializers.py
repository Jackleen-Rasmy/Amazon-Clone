from rest_framework import serializers
from .models import Product, Brand, ProductImages, Review
from taggit.serializers import TagListSerializerField, TaggitSerializer


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
        
class ProductListSerializer(TaggitSerializer, serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    tags = TagListSerializerField()

    class Meta:
        model = Product
        fields = ['name', 'flag', 'price', 'image','sku','tags','subtitle','description','brand', 'review_count', 'avg_rate']
        
    
        
class ProductDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    images = ProductImagesSerializer(source='product_image',many=True)
    reviews = ReviewSerializer(source='review_product',many=True)
    tags = TagListSerializerField()
    
    class Meta:
        model = Product
        fields = ['name', 'flag', 'price', 'image', 'sku', 'tags', 'subtitle', 'description', 'brand', 'review_count', 'avg_rate', 'images', 'reviews']


          
class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'         