# Import necessary libraries
import os
import requests

SHEETY_API_KEY = os.getenv("SHEETY_API_FLIGHT")


class DataManager:
    """A class to represent all the functionalities
    of the Sheety API."""
    def __init__(self):
        self.ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/włochy/loty"

    def sheety_get_response(self):
        """Function to get the response from google sheet"""
        response = requests.get(url=self.ENDPOINT)
        response.raise_for_status()
        data = response.json()
        return data

    def sheety_put_request(self, row_id: int, iata_code: str, link: str, price_pln: float, all_data: str):
        """Function to update flight data"""
        params = {
            "loty": {
                "cityToIata": iata_code,
                "flightLink": link,
                "pricePln": price_pln,
                "flightData": all_data,
            }
        }
        response = requests.put(url=f"{self.ENDPOINT}/{row_id}", json=params)
        print(response.text)
