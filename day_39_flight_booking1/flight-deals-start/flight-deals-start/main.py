#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch


SHEETY_ENDPOINT = "https://api.sheety.co/755b3d11bce3f82747c13489820150d0/copyOfFlightDeals/prices"
FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com" 
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/755b3d11bce3f82747c13489820150d0/copyOfFlightDeals/prices"
SHEETY_DELETE_ENDPOINT = "https://api.sheety.co/755b3d11bce3f82747c13489820150d0/copyOfFlightDeals/prices/"
flight_api_key = "PCgbo1vt9rFZRgVSQE4dl1TUgPnSKGUz"


parameters = {"flight_api_key":flight_api_key}


sheet_data = DataManager(SHEETY_ENDPOINT)
sheet_data_update = DataManager(SHEETY_PRICES_ENDPOINT)
list_of_data = sheet_data.get_data()
sheet_city_names = DataManager(SHEETY_ENDPOINT)
flight_search_data = FlightSearch()
sheety_iatacode_update = DataManager(SHEETY_PRICES_ENDPOINT)
sheet_data_delete = DataManager(SHEETY_DELETE_ENDPOINT)

if list_of_data[0]["iataCode"] == "":
    for row in list_of_data:
        row["iataCode"] = flight_search_data.add_testing(row["city"])
    # print(f"sheet_data:\n {sheet_data}")
        sheet_data_update.update_sheety(city=row["iataCode"], object_id=row["id"])
        print(row["iataCode"])

