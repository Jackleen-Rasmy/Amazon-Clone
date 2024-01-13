from django.shortcuts import render, redirect
from .models import Order, OrderDetails, Cart , CartDetails
from products.models import Product

def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "orders/order_list.html",{"orders":orders})


def checkout(request):
    return render(request, 'orders/checkout.html',{})


def add_to_cart(request):
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    cart = Cart.objects.get(user=request.user,status='Inprogress')

    cart_detail, created = CartDetails.objects.get_or_create(cart=cart,product=product)
    
    cart_detail.quantity = quantity
    cart_detail.total = round(product.price * cart_detail.quantity,2)

    cart_detail.save()
    
    return redirect(f'/products/{product.slug}')
    
    
    

    
    
    
    