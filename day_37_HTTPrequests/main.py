import requests
from datetime import datetime

TOKEN = "1234567890qwerty"
USERNAME = "angedu"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Days",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.json())

pixel_creation_value_endpoint =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today)

graph_value = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

# response =  requests.post(url= pixel_creation_value_endpoint, json=graph_value,headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "2"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.json())


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

requests.delete(url=delete_endpoint, headers=headers)