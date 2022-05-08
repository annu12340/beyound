import requests
import json


def create_asset(intent, asset_name, description):
    print("*"*20)
    print('Creating asset')
    print("-"*20)
    print("\n"*5)
    url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/projects/589cc172-87c0-43db-afb9-fcbbf79d693b/assets"
    payload = {
        "qrCodes": [
            {
                "dynamicRedirectType": "SCAN_ID_IN_QUERY_STRING_PARAMETER",
                "intent": intent,
                "intentType": "DYNAMIC_REDIRECT",
                "locatorKeyType": "SHORT_URL",
                "status": "ACTIVE"
            }
        ],
        "description": description,
        "name": asset_name
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJraWQiOiJ4ZFFwRkoxVDRRWnJMWXJYVHR4VVA5SVUxMGh3M240K0FTS1hWcWxaZkNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNWY5NGEyYS1lNGJjLTRiYmMtYjRjMi05NDA2M2I3MjAyNjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Bd2ZOUzA4bHMiLCJjbGllbnRfaWQiOiI2MXJrM3JhOW9sbjJhMDhlMm9oNG12dnE3ayIsIm9yaWdpbl9qdGkiOiJmZTFjZTg2ZS03NTkzLTQ5OGMtYWJlZi0yMTc3YjcyMzhkZjMiLCJldmVudF9pZCI6ImM3YTgxZGRkLTZhMDEtNGQ4Ny1iNjUxLWI0MmMwZjMxNGExNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTIwMDkwNjgsImV4cCI6MTY1MjA1MjI2OCwiaWF0IjoxNjUyMDA5MDY4LCJqdGkiOiI5OThjNjQ5Mi0xNTRmLTQ0YzAtOWNmNC0xZDUzZmQ1ZjNiZDgiLCJ1c2VybmFtZSI6Inp4aTZ4cXdhYXJyY3JkeXZteCJ9.KpjzUkoPBjVvvKHQluZjyQQk_8K8uDRzoH_nKwL2rq81MasUNvxQOHDuuJ7_K5mt9Q9KtRh6rpjUVGiWxl56dPkIYjPU724wkYXqx77Vmxrm9k4hLh_xmahOqsy4Xyw5sToQY6cOwo2HFKsSeHD3HTQE9f86RRZz1fV20vK-_GpzfOZevHuElbhvtLFfAUUUtsoilQDgqzIJatmqw6i5AL8ZMXy2hU7iIkC9hpzgMkdP9ogkp0nLdhwZvVo75HO6k9HSELngBhfG_2JWpLhwnsiBm4EH68OTlGUyvlpEqbOXRUKsg69u3rT7JzCC7QeeI8917KS7Q37vvQqAZzUJQA"

    }
    response = requests.post(url, json=payload, headers=headers)
    json_object = json.loads(response.text)
    result = json.dumps(json_object, indent=3)
    print("new assest", result)
    return result


create_asset("http://127.0.0.1:8000/raffle",
             "QR code raffle", "raffle decription")
