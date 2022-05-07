# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')

# client = Client(account_sid, auth_token)


# call = client.calls.create(
#     twiml='<Response><Say>HEY help. My child is missing since morning !</Say></Response>',

#     from_='+19362263441',
#     to='+919188058865'
# )
# print(call)
