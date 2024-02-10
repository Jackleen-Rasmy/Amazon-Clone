from django.shortcuts import render, redirect
from .forms import SignupForm, UserActivationForm
from django.core.mail import send_mail
from .models import Profile
from django.contrib.auth.models import User
from products.models import Product, Brand, Review
from orders.models import Order


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save(commit=False)
            user.is_active = False
            
            form.save()
            profile = Profile.objects.get(user__username=username)

            

            # Send the email
            # print(email)
            send_mail(
                "activate your account",
                f"Welcome {username} \nUse this code {profile.code} to activate your account",
                "jacky@gmail.com",
                [email],
                fail_silently=False,
            )

    
            return redirect(f'/accounts/{username}/activate')
        
    else:
        form = SignupForm()
        
    return render(request, "accounts/signup.html", {'form':form})



def user_activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.code = ''
                user = User.objects.get(username=username)
                user.is_active = True
                
                user.save()
                profile.save()
                return redirect('/accounts/login')
            
    else:
        form = UserActivationForm()
    return render(request, 'accounts/activate.html', {'form':form})
            
        
        
def dashboard(request):
    users = User.objects.all().count()
    products = Product.objects.all().count()
    brands = Brand.objects.all().count()
    orders = Order.objects.all().count()
    reviews = Review.objects.all().count()
    new_products = Product.objects.filter(flag='New').count()
    sale_products = Product.objects.filter(flag='Sale').count()
    feature_products = Product.objects.filter(flag='Feature').count()
    
    
    
    
    return render(request, 'accounts/dashboard.html', {
        'users':users,
        'products':products,
        'brands':brands,
        'orders':orders,
        'reviews':reviews,
        'new_products':new_products,
        'sale_products':sale_products,
        'feature_products':feature_products
    })
