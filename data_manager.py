import requests
from pprint import pprint

sheety_api_enpoint = "https://api.sheety.co/b9c8aa7fec7d25fc72163473e07f2a42/flightDeals/prices/"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(sheety_api_enpoint)
        data = response.json()
        self.destination_data = data
        return self.destination_data["prices"]

    def update_sheet(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_api_enpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)