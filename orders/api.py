from rest_framework import generics  
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import datetime
from rest_framework.response import Response
from rest_framework import status


from .serializers import OrderListSerializer, CartListSerializer, CouponSerializer
from .models import Order , Cart , Coupon, CartDetails , OrderDetails
from settings.models import DeliveryFee
from accounts.models import Address
from products.models import Product


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
                
                
                
class CreateOrderAPI(generics.GenericAPIView):
    
    def post(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        code = request.data['payment_code']
        address = request.data['address_id']
        
        cart = Cart.objects.get(user=user, status="Inprogress")
        cart_detail = CartDetails.objects.filter(cart=cart)
        user_address = Address.objects.get(id=address)
        
        # cart | order 
        new_order = Order.objects.create(
            user = user,
            status = 'Recieved',
            code = code,
            delivery_address = user_address,
            coupon = cart.coupon,
            total = cart.cart_total,
            total_with_coupon = cart.total_with_coupon
            
        )
        
        # cart detail | order detail
        for item in cart_detail:
            product = Product.objects.get(id=item.product.id)
            
            OrderDetails.objects.create(
                order = new_order,
                product = product,
                quantity = item.quantity,
                price = product.price,
                total = round(item.quantity * product.price,2)
            )
            
            # decrease product quantity
            product.quantity -= item.quantity
            product.save()
            
        # close cart
        cart.status = 'Completed'
        cart.save()
        
        # send email
        
        return Response({'message': 'order created successfully'}, status=status.HTTP_201_CREATED)
            
        

class CartCreateUpdateDelete(generics.GenericAPIView):
    
    def get(self,request,*args,**kwargs): # get or create
        user = User.objects.get(username=self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=user,status='Inprogress')
        data = CartListSerializer(cart).data
        return Response({'carts':data})
    
    
    def post(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = Product.objects.get(id=request.data['product_id'])
        quantity = int(request.data['quantity'])
        
        cart = Cart.objects.get(user=user,status='Inprogress')
        cart_detail, created = CartDetails.objects.filter(cart=cart, product=product)
        
        cart_detail.quantity = quantity
        cart_detail.total = round(product.price*cart_detail.quantity,2)
        cart_detail.save()
        
        return Response({'message':'cart was updated successfully'}, status=status.HTTP_200_OK)
        
        
    def delete(self,request,*args,**kwargs): # delete from cart
        user = User.objects.get(username=self.kwargs['username'])
        product = CartDetails.objects.get(id=request.data['item_id'])
        product.delete()
        return Response({'message':'product deleted successfully'}, status=status.HTTP_200_OK)