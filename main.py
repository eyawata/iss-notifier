from datetime import datetime

import requests

# Mt. Fuji Coordinates

fuji_lat = 35.363602
fuji_long = 138.726379

parameters = {
    "lat": fuji_lat,
    "lng": fuji_long,
    "tzid": "Asia/Tokyo",
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = datetime.now()


# ISS API FETCH
# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# position = data["iss_position"]
# latitude = position["latitude"]
# longitude = position["longitude"]

# coordinates = (latitude, longitude)

# print(coordinates)
