import requests
import os

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["USER_TOKEN"]

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

requests.post(url=graph_endpoint, )
