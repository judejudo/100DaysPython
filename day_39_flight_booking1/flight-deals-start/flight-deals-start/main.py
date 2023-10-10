#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from  dotenv import load_dotenv
import os

load_dotenv()
SHEETY_ENDPOINT = "https://api.sheety.co/755b3d11bce3f82747c13489820150d0/copyOfFlightDeals/prices"
FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/locations/query" 
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/755b3d11bce3f82747c13489820150d0/copyOfFlightDeals/prices"
API_KEY = os.environ.get("API_KEY")


sheet_data = DataManager(SHEETY_ENDPOINT)
sheet_data_update = DataManager(SHEETY_PRICES_ENDPOINT)
list_of_data = sheet_data.get_data()
sheet_city_names = DataManager(SHEETY_ENDPOINT)
sheety_iatacode_update = DataManager(SHEETY_PRICES_ENDPOINT)
flight_search = FlightSearch(endpoint=FLIGHT_SEARCH_ENDPOINT)

if list_of_data[0]["iataCode"] == "":
    for row in list_of_data:
        response = flight_search.add_iata_code(term=row["city"],location_types="city",api_key=API_KEY)
        iata_code = response["locations"][0]["code"]
        sheet_data_update.update_sheety(city=iata_code, object_id=row["id"])


