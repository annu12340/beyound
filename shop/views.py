from django.shortcuts import render
from .models import Category, Product


def shop_page(request):
    category = Category.objects.all()
    products = Product.objects.filter(is_draft=False)
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
    if request.POST:
        print("********************************")
        name = request.POST['name']
        relationship = request.POST['relationship']
        streetaddress = request.POST['streetaddress']
        phone = request.POST['phone']
        towncity = request.POST['towncity']
        postcode = request.POST['postcode']

        print(name, phone, streetaddress)
        data = 'This is the '+relationship+" of "+name+'\n Phone: '+phone + \
            '\n\n Address: '+streetaddress + "\n"+towncity + "\n"+postcode

        return render(request, 'checkout.html')
    return render(request, 'checkout.html')
