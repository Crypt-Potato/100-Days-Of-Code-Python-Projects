import os
import requests

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

query = input("Input you exercises: ")

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

json = {
    "query": query,
    "gender": os.environ["GENDER"],
    "weight_lb": os.environ["WEIGHT"],
    "height_in": os.environ["HEIGHT"],
    "age": os.environ["AGE"]
}


