import requests

url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/auth/getAccessToken"

payload = {
    "accessKey": "ZXI6XqwaaRRcRDYvMx",
    "accessSecret": "dV7XGkh24hCje6QWYsvhbGMX"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

#
