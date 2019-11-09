# Works if you make the api call through python
from getRoute import getRoute
import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyB2UYBQZJIIb4bIHYnw858xSM6QWwj5CbI')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via walking
now = datetime.now()
dr = gmaps.directions("North Garage Princeton",
                      "Friend Center Princeton",
                      mode="walking",
                      departure_time=now)


# gets the location per step                  #Change this for the number of steps
# when running from python add an extra 0 becasue its a list at beginning
# (dr[0]["legs"][0]["steps"][0]["end_location"])
print(getRoute(dr))
