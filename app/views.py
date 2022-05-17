import imp
from itertools import product
from queue import Empty
import re
from unicodedata import category
import django
from urllib import request
from distutils.log import error
from multiprocessing import context
from django import views
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from numpy import empty, save
from app.models import Product, Customer
from app.forms import RegistrationForm, LoginForm, PasswordChangeForm, CustomerAddressForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User



class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        shoes = Product.objects.filter(category='S')
        beauty_product = Product.objects.filter(category='BEA')
        grocery = Product.objects.filter(category='GRO')
        coffee = Product.objects.filter(category='CO')
        accessory = Product.objects.filter(category='Acce')
        context={
        "topwears":topwears,
        "bottomwear":bottomwear,
        "coffee":coffee,
        "shoes":shoes,
        "beauty_product":beauty_product,
        "grocery":grocery,
        'accessory':accessory,
        }
        return render(request, 'app/home.html',context)

def product_detail(request,pk):
    product = get_object_or_404(Product, id=pk)
    if product.img2 and product.img3 and product.img4:
        img2 = product.img2.url
        img3 = product.img3.url
        img4 = product.img4.url
    else:
        img2 = "#"
        img3 = "#"
        img4 = "#"
   
    context = {
        'product':product,
        'img2':img2,
        'img3':img3,
        'img4':img4,
    }
    return render(request, 'app/productdetail.html', context)

@login_required(login_url="/login")
def buy_now(request):
    return render(request, 'app/buynow.html')

@login_required(login_url="/login")
def mobile(request):
    return render(request, 'app/mobile.html')

@login_required(login_url="/login")
def checkout(request):
    return render(request, 'app/checkout.html',context)

def customerregistration(request):
    if request.method == "POST":
        signup = RegistrationForm(request.POST)
        if signup.is_valid() and signup.cleaned_data['password'] == signup.cleaned_data['confirm_password']:
            fname = signup.cleaned_data['first_name']
            sname = signup.cleaned_data['last_name']
            username = signup.cleaned_data['username']
            email = signup.cleaned_data['email']
            password = signup.cleaned_data['password']

            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = sname
            user.save()
            messages.success(request,"Wecome to Koffette")
            return redirect("/login")
        elif signup.cleaned_data['password'] != signup.cleaned_data['confirm_password']:
            messages.error(request, "Password does not match")

    signup = RegistrationForm()
    context = {
        'signup':signup
    }
    return render (request, 'app/customerregistration.html', context)

def login(request):
    if request.method == "POST":
        login = LoginForm(request.POST)
        if login.is_valid():
            username = login.cleaned_data['username']
            password = login.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request,"Welcome To Koffette")
                return redirect('/profile')
            else: 
                messages.error(request, "Invalid Username Or Password")
    login = LoginForm()            
    context={
        "login":login
    }
    return render(request, 'app/login.html',context)

def LogOut(request):
    logout(request)
    messages.error(request,"You Are Logged Out")
    return redirect('/login')

def coffee(request, data = None):
    if data == None:
        coffee = Product.objects.filter(category="CO")
    elif data == 'below':
        coffee = Product.objects.filter(category = "CO").filter(selling_price__lt=1000)
    elif data == 'above':
        coffee = Product.objects.filter(category = "CO").filter(selling_price__gt=1000)
    context = {
        'coffee':coffee,
    }
    return render(request, "app/coffee.html",context)

def clothes(request, data = None):
    topwears = Product.objects.filter(category='TW')
    bottomwear = Product.objects.filter(category='BW')
    if data == "Top":
        topwears = Product.objects.filter(category="TW")
    elif data == "Bottom":
        bottomwear = Product.objects.filter(category="BW")
    elif data == "below":
        bottomwear = Product.objects.filter(category="BW").filter(selling_price__lt=1000) 
    elif data == "below":
        topwears = Product.objects.filter(category="BW").filter(selling_price__lt=1000) 
    elif data == "above":
        bottomwear = Product.objects.filter(category="BW").filter(selling_price__gt=1000) 
    elif data == "above":
        topwears = Product.objects.filter(category="BW").filter(selling_price__gt=1000) 
    context = {
        "topwears":topwears,
        "bottomwear":bottomwear,
        # "clothes":clothes,
    }
    return render(request, "app/clothes.html",context)

def shoes(request):
    shoes = Product.objects.filter(category='S')
    context = {
        "shoes":shoes,
    }
    return render(request, "app/shoes.html",context)
 
def beauty_product(request):
    beauty_product = Product.objects.filter(category='BEA')
    context = {
        "beauty_product":beauty_product,
    }
    return render(request, "app/beauty_products.html",context)

def grocery(request):
    grocery = Product.objects.filter(category='GRO')
    context = {
        "grocery":grocery,
    }
    return render(request, "app/grocery.html",context)

def accessories(request):
    accessory = Product.objects.filter(category='Acce')
    context = {
        'accessory':accessory,
    }
    return render(request, "app/accessories.html",context)


@login_required(login_url="/login")
def orders(request):
    return render(request, 'app/orders.html')


# @login_required(login_url="/login")
class ProfileView(View):
    def get(self, request):
        forms = CustomerAddressForm()
        context = {
            'forms':forms,
        }
        return render(request, 'app/profile.html',context)

    def post(self, request):
        if request.method == "POST":
            forms = CustomerAddressForm(request.POST)
            if forms.is_valid():
                current_user = request.user
                name = forms.cleaned_data['name']
                locality = forms.cleaned_data['locality']
                state = forms.cleaned_data['state']
                city = forms.cleaned_data['city']
                pincode = forms.cleaned_data['pincode']

                address = Customer(user=current_user, name=name, locality=locality, state=state, city=city, pincode=pincode)
                address.save()
                messages.success(request, "Congratulations !! Profile Updated Successfully.")
        
        forms = CustomerAddressForm()
        context = {
            'forms':forms
        }
        return render(request, 'app/profile.html',context)


@login_required(login_url="/login")
def address(request):
    address = Customer.objects.filter(user = request.user)
    context = {"address":address}
    return render(request, 'app/address.html', context)


from app.models import Cart
@login_required(login_url="/login")
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(product=product, user=user).save()
    return redirect('/cart')

@login_required(login_url="/login")
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)

        amount = 0.0
        totalamount = 0.0
        shipping_price = 70.0
        discount = 0.0
        selling_price = 0.0
        # Python - List Comprehension
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity*p.product.actual_price)
                amount += tempamount

                temp_discount = (p.quantity*p.product.selling_price)
                selling_price += temp_discount

                if (selling_price >= 500):
                    shipping_price = 0.0
                else:
                    shipping_price = 70.00
                totalamount = selling_price+shipping_price
                discount = amount-selling_price
                save = int(discount-shipping_price)
        else:
            cart = None
            save = 0
            shipping_price = "0.0"

    context = {
        "carts":cart,
        "totalamount":totalamount,
        "amount":amount,
        "shipping_price":shipping_price,
        "discount":discount,
        "save":save
    }
    return render(request, 'app/addtocart.html',context)




from django.db.models import Q
from django.http import JsonResponse
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))

        # cart_item.quantity += 1
        cart_item.quantity -= 1
        cart_item.save()
        
        amount = 0
        totalamount = 0
        shipping_price = 70
        discount = 0
        selling_price = 0
        # Python - List Comprehension
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.actual_price)
            amount += tempamount
        
            temp_discount = (p.quantity*p.product.selling_price)
            selling_price += temp_discount

            if (selling_price >= 500):
                shipping_price = 0
            else:
                shipping_price = 70
            totalamount = selling_price+shipping_price
            discount = amount-selling_price
            save = int(discount-shipping_price)


        data = {
            "quantity":cart_item.quantity,
            "totalamount":totalamount,
            "amount":amount,
            # "shipping_price":shipping_price,
            "discount":discount,
            "save":save
        }
        return JsonResponse(data)
  
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))

        cart_item.quantity += 1
        # cart_item.quantity -= 1
        cart_item.save()
        
        amount = 0
        totalamount = 0
        shipping_price = 70
        discount = 0
        selling_price = 0
        # Python - List Comprehension
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.actual_price)
            amount += tempamount
        
            temp_discount = (p.quantity*p.product.selling_price)
            selling_price += temp_discount

            if (selling_price >= 500):
                shipping_price = 0
            else:
                shipping_price = 70
            totalamount = selling_price+shipping_price
            discount = amount-selling_price
            save = int(discount-shipping_price)


        data = {
            "quantity":cart_item.quantity,
            "totalamount":totalamount,
            "amount":amount,
            # "shipping_price":shipping_price,
            "discount":discount,
            "save":save
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart_item.delete()
        
        amount = 0
        totalamount = 0
        shipping_price = 70
        discount = 0
        selling_price = 0
        # Python - List Comprehension
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.actual_price)
            amount += tempamount
        
            temp_discount = (p.quantity*p.product.selling_price)
            selling_price += temp_discount

            if (selling_price >= 500):
                shipping_price = 0
            else:
                shipping_price = 70
            totalamount = selling_price+shipping_price
            discount = amount-selling_price
            save = int(discount-shipping_price)

        data = {
            # "totalamount":totalamount,
            # "amount":amount,
            # "shipping_price":shipping_price,
            # "discount":discount,
            # "save":save
        }
        return JsonResponse(data)