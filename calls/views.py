from django.shortcuts import render
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

from dotenv import load_dotenv


load_dotenv()


def calls(request):
    if request.POST:
        print("********************************")
        name = request.POST['name']
        age = request.POST['age']
        time = request.POST['time']
        location = request.POST['location']
        wearing = request.POST['wearing']
        extra_info = request.POST['extra_info']
        msg = "My child {0}, aged {1} is missing since {2} from {3}. Zee is wearing a {4}. ".format(
            name, age, time, location, wearing)
        police_fir = "Hello officer. I would like to register a complaint."+msg
        whatsapp_msg = "Hello\n"+msg + \
            "Please, if you have any information about my child, message me immediately"

        account_sid = os.getenv('account_sid')
        auth_token = os.getenv('auth_token')
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            twiml='<Response><Say>HEY help. My child is missing since morning !</Say></Response>',

            from_='+19362263441',
            to=number
        )
        print(call)
# 919188058865

    return render(request, 'twilio_call.html')
