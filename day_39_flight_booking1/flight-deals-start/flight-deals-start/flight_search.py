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