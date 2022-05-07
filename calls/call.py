# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.twiml.voice_response import VoiceResponse, Say
import os
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')

client = Client(account_sid, auth_token)

a = 12343

response = VoiceResponse()
s = 'Hello '+str(a)
response.say(s, voice='alice')
response.record(timeout=10, transcribe=True)


# call = client.calls.create(
#     twiml=response,

#     from_='+19362263441',
#     to='+919188058865'
# )
message = client.messages.create(
    body=s,
    from_='whatsapp:+14155238886',
    to='whatsapp:+919188058865'

)
