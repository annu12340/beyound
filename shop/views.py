from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Category, Product
import stripe


def shop_page(request):
    category = Category.objects.all()
    products = Product.objects.filter()
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/shop.html', context)


def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    ctg = Category.objects.get(name=product_details.category)
    related_products = Product.objects.filter(category=ctg)
    context = {
        'product': product_details,
        'related_products': related_products
    }

    return render(request, 'shop/product-details.html', context)


def checkout(request):
    return render(request, 'checkout.html')


def raffle(request):
    return render(request, 'raffle.html')
