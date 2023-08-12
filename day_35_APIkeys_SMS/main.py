import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "17cf92921d38cf90810e5c27b7490263"

account_sid = "AC149876bcc32b1d9df6810d9c4fc0e881"
auth_token = "99841c7f2761a5fe7b04915fe3b9fd23"
num = 0
while num < 50 :
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Wewe tafuta pesa banaaa",
    from_="+15076328931",
    to="+254110952788"
    )
    num = num + 1

print(message.status)



weather_parameters = {
    "lat": -1.307909,
    "lon": 36.818835,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)