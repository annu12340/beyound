from django.shortcuts import render
from .models import Qrcode_info
# Create your views here.


def qrcode(request):
    if request.POST:
        print("********************************")
        parent = request.POST['parent']
        childname = request.POST['childname']

        relationship = request.POST['relationship']
        streetaddress = request.POST['streetaddress']
        phone = request.POST['phone']
        towncity = request.POST['towncity']
        postcode = request.POST['postcode']
        form = Qrcode_info(parent=parent, childname=childname,  relationship=relationship, streetaddress=streetaddress,
                           towncity=towncity, postcode=postcode, phone=phone)
        form.save()

        return render(request, 'checkout.html')
    return render(request, 'qrcode/qrcode_generation.html')


def qrcode_detail(request, qrcode_id):
    qrcode_details = Qrcode_info.objects.get(id=qrcode_id)
    context = {'qrcode_details': qrcode_details, }
    return render(request, 'qrcode/qrcode_details.html', context)
