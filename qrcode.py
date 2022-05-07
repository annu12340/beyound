from dotenv import load_dotenv
import requests
import os
url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/auth/getAccessToken"

load_dotenv()
payload = {
    "accessKey": os.getenv('accessKey'),
    "accessSecret": os.getenv('accessSecret')
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.text)
