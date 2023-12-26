from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Review, ProductImages, Brand
from django.db.models import Q, F , Value
from django.db.models.aggregates import Count, Min, Max, Avg, Sum


class ProductList(ListView):
    model = Product
    paginate_by = 50
    
    
class ProductDetail(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["images"] = ProductImages.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    
    
    
class BrandList(ListView):
    model = Brand
    paginate_by = 50
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))
    
    
class BrandDetail(ListView):
    model = Product
    template_name = "products/brand_detail.html"
    paginate_by = 50
    
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    
def mydebug(request):
    # data = Product.objects.all()
    # column number --------------------
    # data = Product.objects.filter(price=20)
    # data = Product.objects.filter(price__gt=98) # greater than
    # data = Product.objects.filter(price__gte=98) # greater than or equal
    # data = Product.objects.filter(price__lt=98)  # less than
    # data = Product.objects.filter(price__range=(80,83))
    
    # relation ------------------------
    # data = Product.objects.filter(brand__id=5)
    # data = Product.objects.filter(brand__id__gt=200)
    # data = Product.objects.filter(brand__id__slug=)  
    
    
    # text -----------------------------------
    # data = Product.objects.filter(name__contains='vanessa')
    # data = Product.objects.filter(name__startswith='vanessa')
    # data = Product.objects.filter(name__endswith='Stewart')         
    # data = Product.objects.filter(price__isnull=True)
    
    # date ----------------------------------
    # data = Product.objects.filter(date_column__year=2022)
    # data = Product.objects.filter(date_column__month=4) 
    # data = Product.objects.filter(date_column__day=18)
    
    # complex queries ------------------------------- 
    # data = Product.objects.filter(flag='New' , price__gt=98)
    # data = Product.objects.filter(flag='New').filter(price__gt=98)
    # data = Product.objects.filter(Q(flag='New') & Q(price__gt=98)) # and
    # data = Product.objects.filter(Q(flag='New') | Q(price__gt=98)) # or
    # data = Product.objects.filter(
    #     ~ Q(flag='New') |                    # not (~)
    #     Q(price__gt=98)
    # )
    
    # Field Reference
    # data = Product.objects.filter(quantity=F('price'))
    # data = Product.objects.filter(quantity=F('category__id'))
    
    # ordering
       # - ASC
    # data = Product.objects.all().order_by('name')
    # data = Product.objects.order_by('name')
       # - DESC
    # data = Product.objects.order_by('-name')   
    
    # data = Product.objects.filter(price__gt=98).order_by('name')
    # data = Product.objects.filter(price__gt=98).order_by('name')[:10]
    # data = Product.objects.earliest('name')
    # data = Product.objects.latest('name')
    
    # data = Product.objects.values('name','price') # return : dict
    # data = Product.objects.values_list('name','price') # return : tuple
    # data = Product.objects.only('name','price')
    
    # except column
    # data = Product.objects.defer('description','subtitle')
    
    # select Related
    # data = Product.objects.select_related('brand').all() # Foreignkey , one-to-one
    # data = Product.objects.prefetch_related('brand').all() # many to many
    # data = Product.objects.select_related('brand').select_related('category').all()
    # data = Product.objects.select_related('brand').prefetch_related('category').all()
    
    # aggregations
    # data = Product.objects.aggregate(myavg=Avg('price'), mycount=Count('id'))
    
    # annotation
    # data = Product.objects.all().annotate(is_new=Value(0))   
    data = Product.objects.all().annotate(price_with_tax=F('price')*1.15)
    return render(request, "products/debug.html", {'data':data})  