
import os
from django.shortcuts import render
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say
from dotenv import load_dotenv
from .models import Authorities, Neighbours, Friends


load_dotenv()


def twilio_automation(police_fir_msg, whatsapp_msg):

    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    client = Client(account_sid, auth_token)

    response = VoiceResponse()
    response.say(police_fir_msg, voice='alice')
    response.record(timeout=10, transcribe=True)

    call = client.calls.create(
        twiml=response,
        from_='+19362263441',
        to='+919188058865'
    )

    message = client.messages.create(
        body=whatsapp_msg,
        from_='whatsapp:+14155238886',
        to='whatsapp:+919188058865'
    )


def calls(request):
    authorities = Authorities.objects.all()
    neighbors = Neighbours.objects.all()
    friends = Friends.objects.all()
    # print("neighbors", neighbors)
    context = {
        'authorities': authorities,
        'neighbors': neighbors,
        'friends': friends,

    }
    if request.POST:
        print("********************************")
        name = request.POST['name']
        age = request.POST['age']
        time = request.POST['time']
        location = request.POST['location']
        wearing = request.POST['wearing']
        extra_info = request.POST['extra_info']
        msg = "My child {0}, aged {1} is missing since {2} from {3}. She is wearing a {4}. ".format(
            name, age, time, location, wearing)
        police_fir_msg = "Hello officer. I would like to register a complaint."+msg
        whatsapp_msg = "Hello\n"+msg + \
            "Please, if you have any information about my child, message me immediately"
        twilio_automation(police_fir_msg, whatsapp_msg)

    return render(request, 'twilio_call.html', context)
