import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker 
from products.models import Brand , Product, Review
import random


def brand_seed(n):
    fake = Faker()
    images = ['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']
    
    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f"brand/{images[random.randint(0,9)]}"
        )
        
def product_seed(n):
    fake = Faker()
    flag_types = ['New','Sale','Feature']
    images = ['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']
    brands = Brand.objects.all()
    
    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            flag = flag_types[random.randint(0,2)],
            price = round(random.uniform(20.99,99.99),2),
            image = f"product/{images[random.randint(0,9)]}",
            sku = random.randint(100,1000000),
            subtitle = fake.text(max_nb_chars=450),
            description = fake.text(max_nb_chars=4000),
            brand = brands[random.randint(0,len(brands)-1)]
            
        )

# brand_seed(200)
product_seed(1000)
