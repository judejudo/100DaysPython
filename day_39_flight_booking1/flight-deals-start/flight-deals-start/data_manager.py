import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get_data(self):
        response = requests.get(self.endpoint)
        data = response.json()
        return data["prices"]
    
    def get_city_names(self,count):
        data = self.get_data()
        city_name = data[count]
        return city_name
    
    def update_sheety(self,object_id,city):
        new_data = {
            "price": {
                "iataCode": city
            }
        }
        response = requests.put(
            url=f"{self.endpoint}/{object_id}",
            json=new_data
        )
        return response.json()
    
