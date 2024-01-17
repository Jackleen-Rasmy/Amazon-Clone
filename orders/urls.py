from django.urls import path
from .views import order_list, checkout, add_to_cart
from .api import OrderListAPI, OrderDetailAPI

urlpatterns = [
    path('', order_list),
    path('checkout', checkout),
    path('add-to-cart',add_to_cart),
    
    path('api/<str:username>/list', OrderListAPI.as_view()),
    path('api/<str:username>/order/<int:pk>', OrderDetailAPI.as_view()),
    
    ]