import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "vini1durres"
TOKEN = "44F426CA"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_configuration = {
    "id": "grafikuu1",
    "name": "Info-graph",
    "unit": "hours",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

res = requests.post(url=graph_endpoint,json=graph_configuration,headers=headers)
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/grafikuu1"
today = datetime.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How much time did you spend on your computer?"),
}
resp = requests.post(url=pixel_endpoint,json=pixel_params,headers=headers)
print(resp.text)
'''
today = datetime.now()
update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/grafikuu1/{today.strftime('%Y%m%d')}"
update_params = {
    "quantity": "4.6"
}
respo = requests.put(url=update_endpoint,json=update_params,headers=headers)
print(respo.text)
'''