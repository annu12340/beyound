import random
from django.shortcuts import redirect, render
from .models import Category, Product
from .raffle import scaninfo_main


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
    scanid = request.GET.get('scanId', '')
    print(scanid)
    random_number = random.randint(1, 100)
    result = ''
    result = scaninfo_main(scanid, random_number)
    if result == True:
        print("Congrats you are the lucky winner")
    return render(request, 'raffle.html')
