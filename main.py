# Import necessary libraries
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

# Constants
DEPARTURE_CITY = "WARSAW"
DEPARTURE_CITY_IATA_CODE = "WAW"

# Sheety object definition
sheet_data_manager = DataManager()
sheet_data = sheet_data_manager.sheety_get_response()

# Flight data object definition
flight_data_manager = FlightData()

# 1. Update IATA Code of destination cities
# 2. Extract lowest flight price for destination cities
for flight_data in sheet_data["loty"]:
    if flight_data["cityToIata"] == "":
        # Flight search object definition
        flight_search_manager = FlightSearch(city=flight_data["cityTo"])
        location_data = flight_search_manager.kiwi_get_location()
        flight_data["cityToIata"] = location_data["locations"][0]["code"]
        sheet_data_manager.sheety_put_request(flight_data["cityToIata"], flight_data["id"])
    else:
        pass

    # Extract destination city & cheapest flight cost from kiwi API response
    flight_details = flight_data_manager.flight_search_get_request(
        iata_code=flight_data["cityToIata"],
        date_from=flight_data["dateStart"],
        nights_from=flight_data["nightsCountFrom"],
        nights_to=flight_data["nightsCountTo"])
    try:
        flight_id = flight_details[0]["id"]
        price = flight_details[0]["price"]
        outbound_date = flight_details[0]["route"][0]["local_departure"]
        inbound_date = flight_details[0]["route"][1]["local_departure"]
    except IndexError:
        print(f"There's no flight for {flight_data['cityToIata']}")
    else:
        if flight_details:
            sheet_data_manager.sheety_put_request(flight_data["id"],
                                                  iata_code=flight_data["cityToIata"],
                                                  price_pln=price,
                                                  flight_id=flight_id)
