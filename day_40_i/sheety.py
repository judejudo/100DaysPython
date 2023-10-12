import requests

class Sheety:
  def __init__(self, endpoint):
    self.endpoint = endpoint
  
  def update_data(self,data):
    response = requests.post(self.endpoint, json=data)
    return response.json()