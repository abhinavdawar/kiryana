from django.http import HttpResponse
from .models import Categories, Products, Items
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("This is views in inventory")

def get_categories(request):
    categories = Categories.objects.all()
    return render(request,'display_categories.html',{'categories':categories})

def get_products(request):
    products = Products.objects.all()
    return render(request,'display_products.html',{'products':products})

def get_items(request):
    items = Items.objects.all()
    return render(request,'display_items.html',{'items':items})

