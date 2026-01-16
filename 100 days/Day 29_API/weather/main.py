import requests

wm_Endpoint = "http://api.weatherapi.com/v1/current.json"
api_key = "9df02caa238e48228de232333250112"

weather_params = {
    "key": "9df02caa238e48228de232333250112"
}

response = requests.get(wm_Endpoint, params=weather_params)

print(response)
from twilio.rest import Client