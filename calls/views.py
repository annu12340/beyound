from django.shortcuts import render
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

from dotenv import load_dotenv


load_dotenv()


def calls(request):
    if request.POST:
        print("********************************")
        number = request.POST['number']

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
