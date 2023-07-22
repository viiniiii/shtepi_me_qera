import requests
from datetime import datetime
API_ID = "e266cc20"
API_KEY = "081d51f315e35745542f3fcd9c7d45e7"

GENDER = "M"
WEIGHT_KG = "63"
HEIGHT_CM = "174"
AGE = "19"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


sheety_endpoint = "https://api.sheety.co/cd281843c9fbbc6161422a92d8617a87/myWorkout/workouts"
date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

res = requests.post(url=sheety_endpoint,json=sheet_inputs)
print(res.text)