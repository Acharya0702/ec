from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

STATE_CHOICES = (
    ('Andaman & Nicobar Island', 'Andaman & Nicaobar Island'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Asam', 'Asam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chattisgarh', 'Chattisgarh'),
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
    ('Daman & Diu', 'Daman & Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujurat', 'Gujurat'),
    ('Haryana', 'Haryana'),
    ('Himanchal Pradesh', 'Himanchal Pradesh'),
    ('Jammu & kashmir', 'Jammu & kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Keral', 'Keral'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('nagaland', 'nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Panjab', 'Panjab'),
    ('rajasthan', 'rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telengana', 'Telengana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
)

CATEGORY_CHOICES = (
    ('SUV', 'SUV'),
    ('Hatchback', 'Hatchback'),
    ('Sedan', 'Sedan'),
    ('MUV', 'MUV'),
    ('Luxury', 'Luxury'),
)

FUEL_CHOICES = (
    ('Petrol','Petrol'),
    ('Diesel','Diesel'),
    ('CNG','CNG'),
)

SELLER_CHOICES = (
    ('Dealer', 'Dealer'),
    ('Individual','Individual'),
)

TRANSMISSION_MODES = (
    ('Automatic','Automatic'),
    ('Manual','Manual'),
)

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)
YEAR_CHOICES = (
    (1980, 1980),
    (1981, 1981),
    (1982, 1982),
    (1983, 1983),
    (1984, 1984),
    (1985, 1985),
    (1986, 1986),
    (1987, 1987),
    (1988, 1988),
    (1989, 1989),
    (1990, 1990),
    (1991, 1991),
    (1992, 1992),
    (1993, 1993),
    (1994, 1994),
    (1995, 1995),
    (1996, 1996),
    (1997, 1997),
    (1998, 1998),
    (1999, 1999),
    (2000, 2000),
    (2001, 2001),
    (2002, 2002),
    (2003, 2003),
    (2004, 2004),
    (2005, 2005),
    (2006, 2006),
    (2007, 2007),
    (2008, 2008),
    (2009, 2009),
    (2010, 2010),
    (2011, 2011),
    (2012, 2012),
    (2013, 2013),
    (2014, 2014),
    (2015, 2015),
    (2016, 2016),
    (2017, 2017),
    (2018, 2018),
    (2019, 2019),
    (2020, 2020),
    (2021, 2021),
    (2022, 2022),
    (2023, 2023),
    (2024, 2024),
    (2025, 2025),
    (2026, 2026),
    (2027, 2027),
    (2028, 2028),
    (2029, 2029),
    (2030, 2030),
)

class Product(models.Model):
    car_name = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100, default= 'model')
    year = models.IntegerField(choices= YEAR_CHOICES, default=datetime.datetime.now().year)
    selling_price = models.FloatField()
    present_price = models.FloatField()
    kms_driven = models.FloatField(default=0.0)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    fuel_type = models.CharField(choices=FUEL_CHOICES, max_length=10)
    seller_type = models.CharField(choices=SELLER_CHOICES, max_length=10)
    transmission = models.CharField(choices=TRANSMISSION_MODES, max_length=10)
    description = models.TextField()
    product_image = models.ImageField(upload_to='product')
    product_image1 = models.ImageField(upload_to='product', default=0)
    product_image2 = models.ImageField(upload_to='product', default=0)
    product_image3 = models.ImageField(upload_to='product', default=0)
    product_image4 = models.ImageField(upload_to='product', default=0)
    product_image5 = models.ImageField(upload_to='product', default=0)
    product_image6 = models.ImageField(upload_to='product', default=0)
    product_image7 = models.ImageField(upload_to='product', default=0)
    product_image8 = models.ImageField(upload_to='product', default=0)
    def __str__(self) -> str:
        return self.car_name

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self) -> str:
        return self.name
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)