from django.shortcuts import render, redirect
from django.views import View
from . models import Product, Customer, Wishlist
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def home(request):
    wishitem = 0
    product = Product.objects.filter()
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/index.html", locals())

def about(request):
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/about.html", locals())

def contact(request):
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/contact.html", locals())

# @method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request, val):
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
            product = Product.objects.filter(category=val)
            car_name = Product.objects.filter(category=val).values('car_name')
        return render(request, "app/category.html", locals())

# @method_decorator(login_required, name='dispatch')
class CategoryTitle(View):
    def get(self, request, val):
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
            product = Product.objects.filter(car_name=val)
            car_name = Product.objects.filter(category=product[0].category).values('car_name')
        return render(request, "app/category.html", locals())
    
class Brand(View):
    def get(self, request, val):
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
            product = Product.objects.filter(car_brand=val)
            car_name = Product.objects.filter(category=product[0].category).values('car_name')
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    def get(self, request, pk):
        wishitem = 0
        product = Product.objects.get(pk=pk)
        if request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(Q(product = product) & Q(user = request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/productdetail.html", locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/registration.html', locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrats! User Registration Successful.')
        else:
            messages.warning(request, 'Invalid Input Data.')
        return render(request, 'app/registration.html', locals())

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user = user, name = name, locality = locality, mobile = mobile, city = city, state = state, zipcode = zipcode)
            reg.save()
            messages.success(request, 'Congratulations! Profile data saved Successfully.')
        else:
            messages.warning(request, 'Invalid Input Data.')
        return render(request, 'app/profile.html', locals())

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/address.html', locals())

@method_decorator(login_required, name='dispatch')
class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/updateaddress.html', locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, 'Congratulations! Profile Updated Successfully.')
        else:
            messages.warning(request, 'Invalid Input Data.')
        return redirect("address")

@login_required
def show_wishlist(request):
    user = request.user
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Wishlist.objects.filter(user=user)
    return render(request, 'app/wishlist.html', locals())

@login_required
def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user, product=product).save()
        data = {
            'message':'Wishlist Added Successfully',
        }
        return JsonResponse(data)

@login_required
def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data = {
            'message':'Wishlist Remove Successfully',
        }
        return JsonResponse(data)

def search(request):
    lis = []
    query = request.GET['search']
    product_name = Product.objects.filter(Q(car_name__icontains=query))
    product_brand = Product.objects.filter(Q(car_brand__icontains=query))
    product_model = Product.objects.filter(Q(car_model__icontains=query))
    product_category = Product.objects.filter(Q(category__icontains=query))
    for prod in product_name:
        lis.append(prod)
    for prod in product_brand:
        lis.append(prod)
    for prod in product_model:
        lis.append(prod)
    for prod in product_category:
        lis.append(prod)
    s = set((lis))
    product = list((s))
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/search.html", locals())

def AdvancedSearch(request):
    product, product1, product2 = [], [], []
    query1 = request.GET['firstSelect']
    query2 = request.GET['secondSelect']
    title = ""
    if query1 == '1':
        product_brand = Product.objects.filter(Q(selling_price__range=(1.0, 5.0)) | Q(present_price__range=(1.0, 5.0)))
        title = "category in range of (1-5) LAKH"
    elif query1 == '2':
        product_brand = Product.objects.filter(Q(selling_price__range=(5.0, 10.0)) | Q(present_price__range=(5.0, 10.0)))
        title = "category in range of (5-10) LAKH"
    elif query1 == '3':
        product_brand = Product.objects.filter(Q(selling_price__range=(10.0, 20.0)) | Q(present_price__range=(10.0, 20.0)))
        title = "category in range of (10-20) LAKH"
    elif query1 == '4':
        product_brand = Product.objects.filter(Q(selling_price__range=(20.0, 30.0)) | Q(present_price__range=(20.0, 30.0)))
        title = "category in range of (20-30) LAKH"
    elif query1 == '5':
        product_brand = Product.objects.filter(Q(selling_price__range=(3.0, 50.0)) | Q(present_price__range=(3.0, 50.0)))
        title = "category in range of (30-50) LAKH"
    elif query1 == '6':
        product_brand = Product.objects.filter(Q(selling_price__gte=50.0) | Q(present_price__gte=50.0))
        title = "category in range of above 50 LAKH"
    else:
        product_brand = Product.objects.filter(Q(car_brand__icontains=query1))
        title = "model of {} brand".format(query1)
    if query2 == 'SUV' or query2 == 'Hatchback' or query2 == 'Sedan' or query2 == 'MUV' or query2 == 'Luxury':
        product_model = Product.objects.filter(Q(category__icontains = query2))
    else:
        product_model = Product.objects.filter(Q(car_model__icontains = query2))
    for prod in product_brand:
        product1.append(prod)
    for prod in product_model:
        product2.append(prod)
    for x in product2:
        if x in product1:
            product.append(x)
    s = set((product))
    product = list((s))
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/advancedsearch.html", locals())