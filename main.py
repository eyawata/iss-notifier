from datetime import datetime

import requests

# Mt. Fuji Coordinates
MY_LAT = 35.363602
MY_LONG = 138.726379

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def below_iss():
    """
    returns true if current position is within +5 or -5 degrees of the ISS position.
    """

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_diff = abs(MY_LAT - iss_latitude) <= 5
    long_diff = abs(MY_LONG - iss_longitude) <= 5

    return lat_diff or long_diff


def sun_down():
    """
    returns true if sun is down i.e. currently dark
    """

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


if sun_down() and below_iss():
    print("LOOOOOOK UP")
else:
    print("not yet")

    # Then send me an email to tell me to look up.
    # # BONUS: run the code every 60 seconds.

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
