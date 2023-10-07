from  dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("API_KEY")
APP_KEY = os.getenv("APP_KEY")
AGE = os.getenv("AGE")
WEIGHT = os.getenv("WEIGHT")
HEIGHT = os.getenv("HEIGHT")
GENDER = os.getenv("GENDER")

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/755b3d11bce3f82747c13489820150d0/judeWorkouts/workouts"

prompt = input("Please enter your days workout exercise ")
headers = {
    "x-app-id": APP_KEY,
    "x-app-key": API_KEY  
}
params = {
        "query": prompt,
        "gender": GENDER,
        "age": AGE,
        "weight_kg":WEIGHT,
        "height_cm": HEIGHT
    }

current_date = datetime.now()

response = requests.post(nutrition_endpoint, headers=headers, json=params)
json_response = response.json()


for exercise in json_response['exercises']:
    sheety_data = {
        "workout":{
            "date": current_date.strftime("%d/%m/%Y"),
            "time": current_date.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


sheety_response = requests.post(sheety_endpoint,json=sheety_data)
print(sheety_response.json())

if response.status_code == 200 and sheety_response.status_code ==200:
    print("Successfully Created Row in you Googlesheety Data")
