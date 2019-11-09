import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyB2UYBQZJIIb4bIHYnw858xSM6QWwj5CbI')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("7218 Deavers Run Court",
                                     "George Mason University",
                                     mode="driving",
                                     departure_time=now)


# clear
# print(directions_result)
print((directions_result)[0]['routes'])
