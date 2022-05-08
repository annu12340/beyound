import requests
import json
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()


def scaninfo_main(scanid):
    url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/scans/"+scanid

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer eyJraWQiOiJ4ZFFwRkoxVDRRWnJMWXJYVHR4VVA5SVUxMGh3M240K0FTS1hWcWxaZkNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNWY5NGEyYS1lNGJjLTRiYmMtYjRjMi05NDA2M2I3MjAyNjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Bd2ZOUzA4bHMiLCJjbGllbnRfaWQiOiI2MXJrM3JhOW9sbjJhMDhlMm9oNG12dnE3ayIsIm9yaWdpbl9qdGkiOiI2MDg4NjQ3NS1iNzZhLTRkMmEtOWFkNi04MjQ1ZDc1ZDQ1YTMiLCJldmVudF9pZCI6IjMxZmRmMzU1LTE2MTItNDkwYy1iZmJjLTk3NzJhODZkMjhkNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE5NTkyMjQsImV4cCI6MTY1MjAwMjQyNCwiaWF0IjoxNjUxOTU5MjI0LCJqdGkiOiIxYzJjYjQ0NS05MWQyLTQ4NWUtOWVkMy1hOTdkYTI4NWU5OWEiLCJ1c2VybmFtZSI6Inp4aTZ4cXdhYXJyY3JkeXZteCJ9.cDmilpKTcx1F7TWx_VidjbU8ieXKo1QqRCN0B85OTEBpsJmPPi9_WiYW77jpW2xfREGFDGP8wwNvTaQ8LzlQjO9LcUtSActuYxLRX1Zqh37LIUsOPhnSH6YAS3VNXl6LTjyeXN_LDpl-ErkTeUjKoMfkBFJDWSltc9wxNdiZBFcqnp7kynkZ6OtEfkS0tAfUxMoG7XgTenF6s5I1c0UJTkwxdsF_q-hhKhKT-kKdiG5dnrr0LDw6zCOqC3P4UpsbZGX6VfGX_XxNKLEYAbEjJSKY56BpThPkmsdBimqzB7QEijacKF0n2oz8iiBxWh5rqcz6isQ0h4hXpBW454iI7Q"
    }

    response = requests.get(url, headers=headers)

    json_object = json.loads(response.text)
    result = json.dumps(json_object, indent=3)

    print(result)

    time = json_object["scan"]["scanTime"]
    city = json_object["scan"]["locationCityName"]
    region = json_object["scan"]["locationRegionName"]
    country = json_object["scan"]["locationCountryName"]
    latitude = json_object["scan"]["locationLatitude"]
    longitude = json_object["scan"]["locationLongitude"]
    gmap = "https://maps.google.com/?q="+latitude+","+longitude+" "
    msg = "A scan of your child's jewellry from has been made from {},{},{} at {}. The exact latitude and longitude is {},{}".format(
        city, region, country, time, latitude, longitude)
    twilio_contact(msg, gmap)


def twilio_contact(msg, gmap):
    print('calling twilio')
    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    client = Client(account_sid, auth_token)
    response = VoiceResponse()
    response.say(msg, voice='alice')
    call = client.calls.create(
        twiml=response,
        from_='+19362263441',
        to='+919188058865'
    )

    message = client.messages.create(
        body=msg+"\n\n"+gmap,
        from_='whatsapp:+14155238886',
        to='whatsapp:+919188058865'
    )
