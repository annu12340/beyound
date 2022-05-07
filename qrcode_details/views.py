from django.shortcuts import render
from .models import Qrcode_info
# Create your views here.


def qrcode(request):
    if request.POST:
        print("********************************")
        name = request.POST['name']
        relationship = request.POST['relationship']
        streetaddress = request.POST['streetaddress']
        phone = request.POST['phone']
        towncity = request.POST['towncity']
        postcode = request.POST['postcode']
        form = Qrcode_info(name=name, relationship=relationship, streetaddress=streetaddress,
                           towncity=towncity, postcode=postcode, phone=phone)
        form.save()
        print(name, phone, streetaddress)
        data = 'This is the '+relationship+" of "+name+'\n Phone: '+phone + \
            '\n\n Address: '+streetaddress + "\n"+towncity + "\n"+postcode
        print(data)
        return render(request, 'checkout.html')
    return render(request, 'qrcode_generation.html')
