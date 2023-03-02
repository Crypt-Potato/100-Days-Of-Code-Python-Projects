from flight_data import FlightData
import os
import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_KEY = os.environ["TEQUILA_KEY"]

class FlightSearch:

    def __init__(self):
        self.headers = {
            "apikey": TEQUILA_KEY
        }

    def get_dest_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=self.headers, params=query)
        result = response.json()["locations"]
        code = result[0]['code']
        return code

    def check_flights(self, origin_code, dest_code, from_time, to_time):
        flight_searching_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        query = {
            "fly_from": origin_code,
            "fly_to": dest_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=flight_searching_endpoint, headers=self.headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print("No flights found for this booking")
            return

        flight_data = FlightData(
            from_airport=data["route"][0]["flyFrom"],
            from_city=data["route"][0]["cityFrom"],
            to_airport=data["route"][0]["flyTo"],
            to_city=data["route"][0]["cityTo"],
            nights_in_dest=data["nightsInDest"],
            price=data["price"],
            out_date=str(data["route"][0]["local_departure"]).split("T"),
            return_date=str(data["route"][1]["local_arrival"]).split("T")
        )
        print(f"{flight_data.to_city}: £{flight_data.price}")
        return flight_data
