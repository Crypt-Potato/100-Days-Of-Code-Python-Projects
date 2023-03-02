import os
import requests
from pprint import pprint


class DataManager:

    def __init__(self):
        self.authorization_headers = None
        self.data = None
        self.response = None
        self.update_data = None
        self.row_update_endpoint = None
        self.sheety_endpoint = "https://api.sheety.co/31adb5f7f3220ad12ebade7128d63bc7/flightDeals/prices" # MAKE ENV
        # VAR
        
    def get_dest_data(self):
        self.authorization_headers = {
            "Authorization": "Bearer %+9G+3#6T8&A0&)&n9xx$#+9650+5+o&o)%2Z(8!a"  # MAKE ENV VAR
        }
        self.response = requests.get(url=self.sheety_endpoint, headers=self.authorization_headers)
        self.data = self.response.json()['prices']
        return self.data

    def update_rows(self):
        for row in self.data:
            self.row_update_endpoint = f"{self.sheety_endpoint}/{row['id']}"
            self.update_data = {
                "price": {
                    "city": row["city"],
                    "iataCode": row["iataCode"],
                    "lowestPrice": row["lowestPrice"],
                    "id": row["id"]
                }
            }
            self.response = requests.put(url=self.row_update_endpoint, json=self.update_data,
                                         headers=self.authorization_headers)
