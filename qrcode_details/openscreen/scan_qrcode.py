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
        "Authorization": "Bearer eyJraWQiOiJ4ZFFwRkoxVDRRWnJMWXJYVHR4VVA5SVUxMGh3M240K0FTS1hWcWxaZkNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNWY5NGEyYS1lNGJjLTRiYmMtYjRjMi05NDA2M2I3MjAyNjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Bd2ZOUzA4bHMiLCJjbGllbnRfaWQiOiI2MXJrM3JhOW9sbjJhMDhlMm9oNG12dnE3ayIsIm9yaWdpbl9qdGkiOiJmZTFjZTg2ZS03NTkzLTQ5OGMtYWJlZi0yMTc3YjcyMzhkZjMiLCJldmVudF9pZCI6ImM3YTgxZGRkLTZhMDEtNGQ4Ny1iNjUxLWI0MmMwZjMxNGExNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTIwMDkwNjgsImV4cCI6MTY1MjA1MjI2OCwiaWF0IjoxNjUyMDA5MDY4LCJqdGkiOiI5OThjNjQ5Mi0xNTRmLTQ0YzAtOWNmNC0xZDUzZmQ1ZjNiZDgiLCJ1c2VybmFtZSI6Inp4aTZ4cXdhYXJyY3JkeXZteCJ9.KpjzUkoPBjVvvKHQluZjyQQk_8K8uDRzoH_nKwL2rq81MasUNvxQOHDuuJ7_K5mt9Q9KtRh6rpjUVGiWxl56dPkIYjPU724wkYXqx77Vmxrm9k4hLh_xmahOqsy4Xyw5sToQY6cOwo2HFKsSeHD3HTQE9f86RRZz1fV20vK-_GpzfOZevHuElbhvtLFfAUUUtsoilQDgqzIJatmqw6i5AL8ZMXy2hU7iIkC9hpzgMkdP9ogkp0nLdhwZvVo75HO6k9HSELngBhfG_2JWpLhwnsiBm4EH68OTlGUyvlpEqbOXRUKsg69u3rT7JzCC7QeeI8917KS7Q37vvQqAZzUJQA"
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
