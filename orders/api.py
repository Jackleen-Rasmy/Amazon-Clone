from rest_framework import generics  
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import datetime
from rest_framework.response import Response

from .serializers import OrderListSerializer, CartListSerializer, CouponSerializer
from .models import Order , Cart , Coupon
from settings.models import DeliveryFee


class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()
    
    def get_queryset(self):
        queryset = super(OrderListAPI, self).get_queryset()
        user = User.objects.get(username=self.kwargs['username'])
        queryset = queryset.filter(user=user)
        return queryset
    
    
class OrderDetailAPI(generics.RetrieveAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()
    
    def get_queryset(self):
        queryset = super(OrderDetailAPI, self).get_queryset()
        user = User.objects.get(username=self.kwargs['username'])
        queryset = queryset.filter(user=user)
        return queryset
    

class ApplyCouponAPI(generics.GenericAPIView):
    serializer_class = CouponSerializer
    def post(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])  # url
        coupon = get_object_or_404(Coupon, code=request.data['coupon_code']) # request body
        cart = Cart.objects.get(user=user,status='Inprogress')
        deliver_fee = DeliveryFee.objects.last().fee
        
        
        if coupon and coupon.quantity > 0:
            today_date = datetime.datetime.today().date
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = round(cart.cart_total / 100*coupon.discount,2)
                subtotal = cart.cart_total - coupon_value
                
                cart.coupon = coupon
                cart.total_with_coupon = subtotal
                cart.save()
                
                coupon.quantity -= 1
                coupon.save()
                
                return Response({'message': 'coupon was applied successfully'})
            
            else:
                return Response({'message': 'coupon is invalid or expired'})
            
        return Response({'message':'coupon not found'})
                