#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from  dotenv import load_dotenv
from datetime import datetime, timedelta
from twilio.rest import Client
from notification_manager import NotificationManager 
import os

load_dotenv()
SHEETY_ENDPOINT = "https://api.sheety.co/1fefdadf7650b71015a5c873b4339e02/copyOfFlightDeals1/prices"
FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/locations/query" 
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/1fefdadf7650b71015a5c873b4339e02/copyOfFlightDeals1/prices"
FLIGHT_PRICE_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
API_KEY = os.environ.get("API_KEY")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

sheet_data = DataManager(SHEETY_ENDPOINT)
sheet_data_update = DataManager(SHEETY_PRICES_ENDPOINT)
list_of_data = sheet_data.get_data()
sheet_city_names = DataManager(SHEETY_ENDPOINT)
sheety_iatacode_update = DataManager(SHEETY_PRICES_ENDPOINT)
flight_search = FlightSearch(endpoint=FLIGHT_SEARCH_ENDPOINT)
flight_price_search = FlightSearch(FLIGHT_PRICE_SEARCH_ENDPOINT)
notifications = NotificationManager()

# print(list_of_data)
if list_of_data[0]["iataCode"] == "":
    for row in list_of_data:
        response = flight_search.add_iata_code(term=row["city"],location_types="city",api_key=API_KEY)
        iata_code = response["locations"][0]["code"]
        sheet_data_update.update_sheety(city=iata_code, object_id=row["id"])
else:
    for row in list_of_data:
        current_date = datetime.now()
        tomorrow_date = current_date + timedelta(days=1)
        day_180 = current_date + timedelta(days=180)
        response = flight_price_search.get_flight_details(api_key=API_KEY,fly_from="LON",fly_to=row["iataCode"],currency="GBP",date_to=day_180.strftime("%d/%m/%Y"),date_from=tomorrow_date.strftime("%d/%m/%Y"))

        flight_price = response["data"][0]["price"]
        dep_city_name = response["data"][0]["cityFrom"]
        depature_iata_code = response["data"][0]["flyFrom"]
        arrival_city_name = response["data"][0]["cityTo"]
        arrival_iata_code = response["data"][0]["flyTo"]
        outbound_date = response["data"][0]["local_departure"]
        inbound_date = response["data"][0]["local_arrival"] 

        if flight_price <= row["lowestPrice"]:
            notifications.send_notification(client=client,flight_price=flight_price,dep_city_name= dep_city_name,depature_iata_code=depature_iata_code, arrival_city_name=arrival_city_name,arrival_iata_code=arrival_iata_code,outbound_date=outbound_date,inbound_date=inbound_date)


