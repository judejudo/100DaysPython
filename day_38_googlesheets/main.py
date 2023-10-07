from  dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")
APP_KEY = os.getenv("APP_KEY")
AGE = os.getenv("AGE")
WEIGHT = os.getenv("WEIGHT")
HEIGHT = os.getenv("HEIGHT")
GENDER = os.getenv("GENDER")

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
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
response = requests.post(nutrition_endpoint, headers=headers, json=params)

# if response.status_code == 200:
#     print(response.status_code)

print(response.json())