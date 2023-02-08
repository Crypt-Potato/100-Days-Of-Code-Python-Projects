import requests
import os

pixela_endpoint = "https://www.pixel.la/v1/users"

user_token = os.environ["USER_TOKEN"]
username = os.environ["USERNAME"]

user_params = {
    'token': "ufsehfisg3392skefefj39fefje",
    "username": "yugm",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
