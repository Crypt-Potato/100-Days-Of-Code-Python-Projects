import requests
import os
from datetime import datetime

now = datetime.now()

date_input = input("Please put the day that you did it. Format: <year> <month(number)> <day(number)>"
                          "Input \"today\" to use today's date.")

if date_input == "today":
    date_to_put_pixel = now.strftime("%Y%m%d")
else:
    date_inputted = date_input.split()
    date_to_put_pixel = datetime(year=int(date_inputted[0]), month=int(date_inputted[1]), day=int(date_inputted[2])).strftime("%Y%m%d")

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

pixel_data = {
    "date": date_to_put_pixel,
    "quantity": "5"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
