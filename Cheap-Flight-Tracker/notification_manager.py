from flight_data import FlightData
import smtplib
import os

EMAIL = os.environ["EMAIL"]
EMAIL_APP_PASSWORD = os.environ["EMAIL_APP_PASSWORD"]


class NotificationManager:

    def __init__(self):
        self.email = EMAIL
        self.app_password = EMAIL_APP_PASSWORD

    def send_notification(self, flight_data: FlightData, city_sheet_data):
        if flight_data.price < city_sheet_data["lowestPrice"]:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.app_password)
                message = f"Subject:Low Price Alert to fly to {flight_data.to_city}\n\nOnly {flight_data.price} " \
                          f"pounds" \
                          f" to fly from {flight_data.from_city}-{flight_data.from_airport} to " \
                          f"{flight_data.to_city}-{flight_data.to_airport}! Depart on {flight_data.out_date[0]} and " \
                          f"return on " \
                          f"{flight_data.return_date[0]}."
                connection.sendmail(from_addr=self.email, to_addrs=self.email, msg=message)
