# import required modules
import datetime
from suntime import Sun
from geopy.geocoders import Nominatim

# Nominatim API to get latitude and longitude
geolocator = Nominatim(user_agent="geoapiExercises")

# input place
place = "dezful"
location = geolocator.geocode(place)

# latitude and longitude fetch
latitude = location.latitude
longitude = location.longitude
sun = Sun(latitude, longitude)

# date in your machine's local time zone
time_zone = datetime.date(2021, 5, 5)
sun_rise = sun.get_local_sunrise_time(time_zone)
sun_dusk = sun.get_local_sunset_time(time_zone)

# display
print("Sun rise at : ", sun_rise.strftime('%H:%M'))
print("Dusk at : ", sun_dusk.strftime('%H:%M'))


