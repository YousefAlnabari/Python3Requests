import requests
import json

# Set up the URL
url = 'https://api.example.com/endpoint'

# Set up the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_token'
}

# Set up the request body
payload = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'age': 30
}
json_payload = json.dumps(payload)

# Make the POST request
response = requests.post(url, headers=headers, data=json_payload)

# Check the response
if response.status_code == 200:
    print('Request successful!')
    print(response.json())
else:
    print('Request failed!')
    print(response.text)
