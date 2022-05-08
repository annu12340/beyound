# 049a28c9-e11d-4c18-9845-5f3d689d28cb
import json
import requests

url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/assets/ea1094bc-85ee-4d11-a446-e4c95c25540d/qrcodes"

payload = {
    "dynamicRedirectType": "NO_SCAN_ID",
    "intent": "https://twitter.com/",
    "intentType": "DYNAMIC_REDIRECT",
    "locatorKeyType": "SHORT_URL",
    "status": "ACTIVE"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJraWQiOiJ4ZFFwRkoxVDRRWnJMWXJYVHR4VVA5SVUxMGh3M240K0FTS1hWcWxaZkNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNWY5NGEyYS1lNGJjLTRiYmMtYjRjMi05NDA2M2I3MjAyNjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Bd2ZOUzA4bHMiLCJjbGllbnRfaWQiOiI2MXJrM3JhOW9sbjJhMDhlMm9oNG12dnE3ayIsIm9yaWdpbl9qdGkiOiJjMjhkNTM5OC1jOGIyLTQ2MzQtYjRkYS04ZGEzNWU0YjhjYjIiLCJldmVudF9pZCI6IjkxMmM2NWQ3LTQ3ZGEtNDMxMC04M2RmLWI4YTM3M2Y0MGZmZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE5NTc2MjIsImV4cCI6MTY1MjAwMDgyMiwiaWF0IjoxNjUxOTU3NjIyLCJqdGkiOiIxYzhhZGNkZi1hZDUzLTQ4OGQtYjM5Ni0xZDZkNTAyMzMzMTUiLCJ1c2VybmFtZSI6Inp4aTZ4cXdhYXJyY3JkeXZteCJ9.UTwLc6Bt50lvqyzY6WlDLifjGgfXBAIYt7XcKz1VGasSM80BsKNVmamCVeuLhSjyuMxdBI6F4vgib-JsWOwDbepWupfM-0_-Z1Ykp2I33eaqu5bh6BGZZx0bL3iHSoAT9EnyxPLIHsn4DUxUs9PCxQvh6UFOWjXBf4qVltoi_SGY-tdzmyWL3MHJl-eR3E4wIUFOfrKOWJlfRIu7LXH1CQQgJwl0bI31aJ7H_PZUHJxG2K8c-it59nn2XcgbqAJTeLdoHkHEfxy--Fjpuwqn8_3mZ6TU0qdpM8pHoUuksa2WRe-3RVU9Tttd7bpPBLvu5hxKq8UwRiXE93Weembrfg"
}

response = requests.post(url, json=payload, headers=headers)
json_object = json.loads(response.text)

print(json.dumps(json_object, indent=3))
