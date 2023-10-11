import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, endpoint):
        self.endpoint = endpoint
        
        
        
    def add_iata_code(self,term,location_types,api_key):
        response = requests.get(url = self.endpoint,params={
                                                            "term": term,
                                                            "location_types": location_types,
                                                            },headers = {"apikey": api_key})
        return response.json()
    
    def get_flight_details(self,api_key,fly_from, fly_to,currency,date_to,date_from):
        response = requests.get(url = self.endpoint,params={
                                                            "fly_from":fly_from,
                                                            "fly_to":fly_to,
                                                            "date_from": date_from,
                                                            "date_to": date_to,
                                                            "currency":currency}, headers = {"apikey" : api_key} )
        return response.json()