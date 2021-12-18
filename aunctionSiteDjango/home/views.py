from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Product
from django.contrib import messages
from .forms import ProductForm


# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products': products})


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved in db')
        return HttpResponseRedirect('/home')
    else:
        form = ProductForm()
        return render(request, "product-form.html", {'form': form})


