from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
import datetime

from .models import Order, OrderDetails, Cart , CartDetails, Coupon
from products.models import Product
from settings.models import DeliveryFee

def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "orders/order_list.html",{"orders":orders})


def checkout(request):
    cart = Cart.objects.get(user=request.user, status='Inprogress')
    cart_detail = CartDetails.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    
    
    if request.method == 'POST':
        code = request.POST['coupon_code']
        coupon = get_object_or_404(Coupon , code=code)
        
        if coupon and coupon.quantity > 0:
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = cart.cart_total / 100*coupon.discount
                subtotal = cart.cart_total - coupon_value
                total = subtotal + delivery_fee
                
                cart.coupon = coupon
                cart.total_with_coupon = subtotal
                cart.save()
        
                return render(request, 'orders/checkout.html',{
                    'cart_detail':cart_detail,
                    'delivery_fee':delivery_fee,
                    'subtotal':subtotal,
                    'discount':coupon_value,
                    'total':total
                    
                })
                
    subtotal = cart.cart_total
    discount = 0
    total = subtotal + delivery_fee
    return render(request, 'orders/checkout.html',{
                    'cart_detail':cart_detail,
                    'delivery_fee':delivery_fee,
                    'subtotal':subtotal,
                    'discount':discount,
                    'total':total
                    
                })


def add_to_cart(request):
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    cart = Cart.objects.get(user=request.user,status='Inprogress')

    cart_detail, created = CartDetails.objects.get_or_create(cart=cart,product=product)
    
    cart_detail.quantity = quantity
    cart_detail.total = round(product.price * cart_detail.quantity,2)

    cart_detail.save()
    
    return redirect(f'/products/{product.slug}')
    
    
    

    
    
    
    