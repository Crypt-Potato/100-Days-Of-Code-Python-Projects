import os
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_dest_data()
is_iata_code = None

origin_city_iata = "LON"

for row in sheet_data:
    if row["iataCode"] == "":
        is_iata_code = False
        break
    else:
        is_iata_code = True

if not is_iata_code:
    for row in sheet_data:
        row["iataCode"] = flight_search.get_dest_code(row["city"])
        data_manager.data = sheet_data
    data_manager.update_rows()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=(6 * 30))

for dest in sheet_data:
    flight = flight_search.check_flights(
        origin_code=origin_city_iata,
        dest_code=dest["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_now
    )

    notification_manager.send_notification(flight, dest)
