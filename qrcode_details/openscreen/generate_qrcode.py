import json
import requests
from .utils import get_qr_code_id, get_asset_id, get_project_id
# 1. Created an asset and a qr code
# 2. Verifying the qr code is correctly created using show_qr_code
# 3. Get the qr code id and the asset id
# 4. Create a contact object
# 5. Get scanid from url and fetch scan info from it


def main(intent, asset_name, description, parent_name, phone):

    result = create_asset(intent, asset_name, description)
    qrcode_id = get_qr_code_id(result)
    assetid = get_asset_id(result)
    projectid = get_project_id(result)

    img_url = show_qr_code(qrcode_id)

    # create_contact_object(assetid, parent_name, "+13362263441")
    # sendsms(projectid)
    return img_url


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
        "Authorization": "Bearer eyJraWQiOiJ4ZFFwRkoxVDRRWnJMWXJYVHR4VVA5SVUxMGh3M240K0FTS1hWcWxaZkNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNWY5NGEyYS1lNGJjLTRiYmMtYjRjMi05NDA2M2I3MjAyNjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Bd2ZOUzA4bHMiLCJjbGllbnRfaWQiOiI2MXJrM3JhOW9sbjJhMDhlMm9oNG12dnE3ayIsIm9yaWdpbl9qdGkiOiI2MDg4NjQ3NS1iNzZhLTRkMmEtOWFkNi04MjQ1ZDc1ZDQ1YTMiLCJldmVudF9pZCI6IjMxZmRmMzU1LTE2MTItNDkwYy1iZmJjLTk3NzJhODZkMjhkNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE5NTkyMjQsImV4cCI6MTY1MjAwMjQyNCwiaWF0IjoxNjUxOTU5MjI0LCJqdGkiOiIxYzJjYjQ0NS05MWQyLTQ4NWUtOWVkMy1hOTdkYTI4NWU5OWEiLCJ1c2VybmFtZSI6Inp4aTZ4cXdhYXJyY3JkeXZteCJ9.cDmilpKTcx1F7TWx_VidjbU8ieXKo1QqRCN0B85OTEBpsJmPPi9_WiYW77jpW2xfREGFDGP8wwNvTaQ8LzlQjO9LcUtSActuYxLRX1Zqh37LIUsOPhnSH6YAS3VNXl6LTjyeXN_LDpl-ErkTeUjKoMfkBFJDWSltc9wxNdiZBFcqnp7kynkZ6OtEfkS0tAfUxMoG7XgTenF6s5I1c0UJTkwxdsF_q-hhKhKT-kKdiG5dnrr0LDw6zCOqC3P4UpsbZGX6VfGX_XxNKLEYAbEjJSKY56BpThPkmsdBimqzB7QEijacKF0n2oz8iiBxWh5rqcz6isQ0h4hXpBW454iI7Q"

    }
    response = requests.post(url, json=payload, headers=headers)
    json_object = json.loads(response.text)
    result = json.dumps(json_object, indent=3)
    print("new assest", result)
    return result


def show_qr_code(qrcode_id):
    print("*"*20)
    print('Showing qr code')
    print("-"*20)
    print("\n"*5)
    url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/qrcodes/" + \
        qrcode_id+"?format=PNG"
    headers = {"Accept": "application/json",        "Authorization": "Bearer eyJraWQiOiJ4ZFFwRkoxVDRRWnJMWXJYVHR4VVA5SVUxMGh3M240K0FTS1hWcWxaZkNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNWY5NGEyYS1lNGJjLTRiYmMtYjRjMi05NDA2M2I3MjAyNjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Bd2ZOUzA4bHMiLCJjbGllbnRfaWQiOiI2MXJrM3JhOW9sbjJhMDhlMm9oNG12dnE3ayIsIm9yaWdpbl9qdGkiOiI2MDg4NjQ3NS1iNzZhLTRkMmEtOWFkNi04MjQ1ZDc1ZDQ1YTMiLCJldmVudF9pZCI6IjMxZmRmMzU1LTE2MTItNDkwYy1iZmJjLTk3NzJhODZkMjhkNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE5NTkyMjQsImV4cCI6MTY1MjAwMjQyNCwiaWF0IjoxNjUxOTU5MjI0LCJqdGkiOiIxYzJjYjQ0NS05MWQyLTQ4NWUtOWVkMy1hOTdkYTI4NWU5OWEiLCJ1c2VybmFtZSI6Inp4aTZ4cXdhYXJyY3JkeXZteCJ9.cDmilpKTcx1F7TWx_VidjbU8ieXKo1QqRCN0B85OTEBpsJmPPi9_WiYW77jpW2xfREGFDGP8wwNvTaQ8LzlQjO9LcUtSActuYxLRX1Zqh37LIUsOPhnSH6YAS3VNXl6LTjyeXN_LDpl-ErkTeUjKoMfkBFJDWSltc9wxNdiZBFcqnp7kynkZ6OtEfkS0tAfUxMoG7XgTenF6s5I1c0UJTkwxdsF_q-hhKhKT-kKdiG5dnrr0LDw6zCOqC3P4UpsbZGX6VfGX_XxNKLEYAbEjJSKY56BpThPkmsdBimqzB7QEijacKF0n2oz8iiBxWh5rqcz6isQ0h4hXpBW454iI7Q"
               }
    response = requests.get(url, headers=headers)
    json_object = json.loads(response.text)
    result = json.dumps(json_object, indent=3)
    img_output = json.loads(result)
    img_url = "data:image/png;base64, "+img_output["image"]["data"]
    print("\n\n\n\n================================", img_url)
    return img_url


def create_contact_object(assetid, parent_name, phone):
    print("*"*20)
    print('Creating contact object')
    print("-"*20)
    print("\n"*5)
    url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/assets/{}/contacts".format(
        assetid)

    payload = {
        "cellPhone": phone,
        "firstName": parent_name[0],
        "lastName": parent_name[1]
    }
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer eyJraWQiOiJ4ZFFwRkoxVDRRWnJMWXJYVHR4VVA5SVUxMGh3M240K0FTS1hWcWxaZkNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNWY5NGEyYS1lNGJjLTRiYmMtYjRjMi05NDA2M2I3MjAyNjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Bd2ZOUzA4bHMiLCJjbGllbnRfaWQiOiI2MXJrM3JhOW9sbjJhMDhlMm9oNG12dnE3ayIsIm9yaWdpbl9qdGkiOiI2MDg4NjQ3NS1iNzZhLTRkMmEtOWFkNi04MjQ1ZDc1ZDQ1YTMiLCJldmVudF9pZCI6IjMxZmRmMzU1LTE2MTItNDkwYy1iZmJjLTk3NzJhODZkMjhkNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE5NTkyMjQsImV4cCI6MTY1MjAwMjQyNCwiaWF0IjoxNjUxOTU5MjI0LCJqdGkiOiIxYzJjYjQ0NS05MWQyLTQ4NWUtOWVkMy1hOTdkYTI4NWU5OWEiLCJ1c2VybmFtZSI6Inp4aTZ4cXdhYXJyY3JkeXZteCJ9.cDmilpKTcx1F7TWx_VidjbU8ieXKo1QqRCN0B85OTEBpsJmPPi9_WiYW77jpW2xfREGFDGP8wwNvTaQ8LzlQjO9LcUtSActuYxLRX1Zqh37LIUsOPhnSH6YAS3VNXl6LTjyeXN_LDpl-ErkTeUjKoMfkBFJDWSltc9wxNdiZBFcqnp7kynkZ6OtEfkS0tAfUxMoG7XgTenF6s5I1c0UJTkwxdsF_q-hhKhKT-kKdiG5dnrr0LDw6zCOqC3P4UpsbZGX6VfGX_XxNKLEYAbEjJSKY56BpThPkmsdBimqzB7QEijacKF0n2oz8iiBxWh5rqcz6isQ0h4hXpBW454iI7Q",

        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    json_object = json.loads(response.text)
    result = json.dumps(json_object, indent=3)
    print(result)

    json_object["projectContact"]["projectId"]


def sendsms(project_id):

    url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/projects'/'smstemplates"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer eyJraWQiOiJ4ZFFwRkoxVDRRWnJMWXJYVHR4VVA5SVUxMGh3M240K0FTS1hWcWxaZkNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNWY5NGEyYS1lNGJjLTRiYmMtYjRjMi05NDA2M2I3MjAyNjQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Bd2ZOUzA4bHMiLCJjbGllbnRfaWQiOiI2MXJrM3JhOW9sbjJhMDhlMm9oNG12dnE3ayIsIm9yaWdpbl9qdGkiOiI2MDg4NjQ3NS1iNzZhLTRkMmEtOWFkNi04MjQ1ZDc1ZDQ1YTMiLCJldmVudF9pZCI6IjMxZmRmMzU1LTE2MTItNDkwYy1iZmJjLTk3NzJhODZkMjhkNSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE5NTkyMjQsImV4cCI6MTY1MjAwMjQyNCwiaWF0IjoxNjUxOTU5MjI0LCJqdGkiOiIxYzJjYjQ0NS05MWQyLTQ4NWUtOWVkMy1hOTdkYTI4NWU5OWEiLCJ1c2VybmFtZSI6Inp4aTZ4cXdhYXJyY3JkeXZteCJ9.cDmilpKTcx1F7TWx_VidjbU8ieXKo1QqRCN0B85OTEBpsJmPPi9_WiYW77jpW2xfREGFDGP8wwNvTaQ8LzlQjO9LcUtSActuYxLRX1Zqh37LIUsOPhnSH6YAS3VNXl6LTjyeXN_LDpl-ErkTeUjKoMfkBFJDWSltc9wxNdiZBFcqnp7kynkZ6OtEfkS0tAfUxMoG7XgTenF6s5I1c0UJTkwxdsF_q-hhKhKT-kKdiG5dnrr0LDw6zCOqC3P4UpsbZGX6VfGX_XxNKLEYAbEjJSKY56BpThPkmsdBimqzB7QEijacKF0n2oz8iiBxWh5rqcz6isQ0h4hXpBW454iI7Q"
    }

    response = requests.get(url, headers=headers)

    print(response.text)
