""" STATUS CODE
    1XX-HOLD ON
    2XX-HERE YOU GO
    3XX-GO AWAY
    4XX-YOU SCREWED UP(REQUEST DOESN'T EXISTS)
    5XX-I(SERVER) SCREWED UP
"""

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "marvellous1@gmail.com"
MY_PASSWORD = "mcvn hrt1 tuag"
MY_LAT = 6.4474
MY_LONG = 3.3903

def is_iss_overhead():
    response = requests.get(url="https://api.open-notify.org/iss-now.json")
    response.raise_for_status() #to raise exceptions for errors
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_position = (iss_longitude, iss_latitude)
    print(iss_position)

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunrise"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up!\n\nThe ISS is above"
        )
