import requests
import os
from datetime import datetime

now = str(datetime.now())

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["USER_TOKEN"]
GRAPH_ID = "graph1"

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Hours Coded Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_creation_config = {
    "date": "".join(now.split()[0].split("-")),
    "quantity": "5"
}

pixel_creation_headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=pixel_creation_headers)
print(response.text)
