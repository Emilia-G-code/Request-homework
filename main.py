import requests

response = requests.get("https://fake-json-api.mock.beeceptor.com")

if(response.status_code == 200):
    print("Here is the website:: \n", response.json())
else:
    print("Error! Wrong request! Please send the correct request!")