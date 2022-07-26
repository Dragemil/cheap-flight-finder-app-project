# Import necessary libraries
import os

import requests

# Constants
KIWI_API_KEY = os.getenv("KIWI_API_KEY")

# Constants
FLY_FROM = "WAW"


class FlightData:
    """A class to represent all the functionalities
    related to flight data"""
    def __init__(self):
        self.ENDPOINT = "https://tequila-api.kiwi.com"
        self.HEADER = {
            "apikey": KIWI_API_KEY,
        }

    def flight_search_get_request(self, iata_code: str, date_from: str, nights_from: int, nights_to: int):
        """Function for getting all the flight data
        for desired destination"""
        params = {
            "fly_from": FLY_FROM,
            "fly_to": iata_code,
            "date_from": date_from,
            "date_to": date_from,
            "nights_in_dst_from": nights_from,
            "nights_in_dst_to": nights_to,
            "flight_type": "round",
            "adults": 2,
            "adult_hold_bag": "1,0",
            "adult_hand_bag": "1,1",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "PLN",
            "locale": "pl",
            "atime_from": "11:00",
            "atime_to": "17:00",
        }
        response = requests.get(url=f"{self.ENDPOINT}/v2/search", headers=self.HEADER, params=params)
        response.raise_for_status()
        data = response.json()
        return data["data"]
