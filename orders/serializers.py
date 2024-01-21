from rest_framework import serializers

from .models import Order, OrderDetails, Cart, CartDetails, Coupon


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'
        
class OrderListSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'    
        
class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetails
        fields = '__all__'
        
class CartListSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'    
        
        
        
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
    