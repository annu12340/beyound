
import json
import requests

url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/projects/589cc172-87c0-43db-afb9-fcbbf79d693b/assets"

payload = {
    "qrCodes": [
        {
            "dynamicRedirectType": "SCAN_ID_IN_QUERY_STRING_PARAMETER",
            "intent": "https://www.google.com/",
            "intentType": "DYNAMIC_REDIRECT",
            "locatorKeyType": "SHORT_URL",
            "status": "ACTIVE"
        }
    ],
    "description": "asset1-descrioption",
    "name": "asset8"
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJraWQiOiJ4ZFFwRkoxVDRRWnJMWXJYVHR4VVA5SVUxMGh3M240K0FTS1hWcWxaZkNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNWY5NGEyYS1lNGJjLTRiYmMtYjRjMi05NDA2M2I3MjAyNjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Bd2ZOUzA4bHMiLCJjbGllbnRfaWQiOiI2MXJrM3JhOW9sbjJhMDhlMm9oNG12dnE3ayIsIm9yaWdpbl9qdGkiOiI2MDg4NjQ3NS1iNzZhLTRkMmEtOWFkNi04MjQ1ZDc1ZDQ1YTMiLCJldmVudF9pZCI6IjMxZmRmMzU1LTE2MTItNDkwYy1iZmJjLTk3NzJhODZkMjhkNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE5NTkyMjQsImV4cCI6MTY1MjAwMjQyNCwiaWF0IjoxNjUxOTU5MjI0LCJqdGkiOiIxYzJjYjQ0NS05MWQyLTQ4NWUtOWVkMy1hOTdkYTI4NWU5OWEiLCJ1c2VybmFtZSI6Inp4aTZ4cXdhYXJyY3JkeXZteCJ9.cDmilpKTcx1F7TWx_VidjbU8ieXKo1QqRCN0B85OTEBpsJmPPi9_WiYW77jpW2xfREGFDGP8wwNvTaQ8LzlQjO9LcUtSActuYxLRX1Zqh37LIUsOPhnSH6YAS3VNXl6LTjyeXN_LDpl-ErkTeUjKoMfkBFJDWSltc9wxNdiZBFcqnp7kynkZ6OtEfkS0tAfUxMoG7XgTenF6s5I1c0UJTkwxdsF_q-hhKhKT-kKdiG5dnrr0LDw6zCOqC3P4UpsbZGX6VfGX_XxNKLEYAbEjJSKY56BpThPkmsdBimqzB7QEijacKF0n2oz8iiBxWh5rqcz6isQ0h4hXpBW454iI7Q"

}
response = requests.post(url, json=payload, headers=headers)
json_object = json.loads(response.text)

print(json.dumps(json_object, indent=3))


# ------
# url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/qrcodes/1ea3034b-88a2-443c-bd04-1c97477ee90c?format=PNG"

# headers = {
#     "Accept": "application/json",
#     "Authorization": "Bearer eyJraWQiOiJ4ZFFwRkoxVDRRWnJMWXJYVHR4VVA5SVUxMGh3M240K0FTS1hWcWxaZkNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNWY5NGEyYS1lNGJjLTRiYmMtYjRjMi05NDA2M2I3MjAyNjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Bd2ZOUzA4bHMiLCJjbGllbnRfaWQiOiI2MXJrM3JhOW9sbjJhMDhlMm9oNG12dnE3ayIsIm9yaWdpbl9qdGkiOiJjMjhkNTM5OC1jOGIyLTQ2MzQtYjRkYS04ZGEzNWU0YjhjYjIiLCJldmVudF9pZCI6IjkxMmM2NWQ3LTQ3ZGEtNDMxMC04M2RmLWI4YTM3M2Y0MGZmZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE5NTc2MjIsImV4cCI6MTY1MjAwMDgyMiwiaWF0IjoxNjUxOTU3NjIyLCJqdGkiOiIxYzhhZGNkZi1hZDUzLTQ4OGQtYjM5Ni0xZDZkNTAyMzMzMTUiLCJ1c2VybmFtZSI6Inp4aTZ4cXdhYXJyY3JkeXZteCJ9.UTwLc6Bt50lvqyzY6WlDLifjGgfXBAIYt7XcKz1VGasSM80BsKNVmamCVeuLhSjyuMxdBI6F4vgib-JsWOwDbepWupfM-0_-Z1Ykp2I33eaqu5bh6BGZZx0bL3iHSoAT9EnyxPLIHsn4DUxUs9PCxQvh6UFOWjXBf4qVltoi_SGY-tdzmyWL3MHJl-eR3E4wIUFOfrKOWJlfRIu7LXH1CQQgJwl0bI31aJ7H_PZUHJxG2K8c-it59nn2XcgbqAJTeLdoHkHEfxy--Fjpuwqn8_3mZ6TU0qdpM8pHoUuksa2WRe-3RVU9Tttd7bpPBLvu5hxKq8UwRiXE93Weembrfg"
# }

# response = requests.get(url, headers=headers)
# print(response.text)
