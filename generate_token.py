import requests

url = "https://kbdgsb6g57.execute-api.us-east-1.amazonaws.com/prod/auth/getAccessToken"

payload = {
    "accessKey": "ZXI6XqwaaRRcRDYvMx",
    "accessSecret": "T2ushh0n4bUt3qZKvjv4s2i6"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
