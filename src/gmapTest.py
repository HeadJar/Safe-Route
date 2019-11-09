import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyB2UYBQZJIIb4bIHYnw858xSM6QWwj5CbI')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
dr = gmaps.directions("North Garage Princeton",
                      "Friend Center Princeton",
                      mode="walking",
                      departure_time=now)


# gets the location per step                  #Change this for the number of steps
# when running from python add an extra 0 becasue its a list at beginning
# (dr[0]["legs"][0]["steps"][0]["end_location"])


l = []
start_loc = (dr[0]["legs"][0]["steps"][0]["start_location"]['lat'],
             dr[0]["legs"][0]["steps"][0]["start_location"]['lng'])
print(start_loc)

l.append(start_loc)
time = dr[0]["legs"][0]["duration"]["text"].split()
# Gets the duration
# Sometimes total time by step is more than duration so add 1

duration = (int(time[0])) + 2
steps = dr[0]["legs"][0]["steps"]

for i in steps:
    t = i["duration"]["text"].split()
    d = (int(t[0]))
    if d > 1:
        start = [i["start_location"]['lat'], i['start_location']['lng']]
        difference_size = [i["end_location"]['lat']-i["start_location"]['lat'],
                           i["end_location"]['lng']-i["start_location"]['lng']]

        step_size_lat = difference_size[0]/d
        step_size_lng = difference_size[1]/d
        for index in range(1, d+1):
            temp = [start[0] + (step_size_lat * index),
                    start[1] + (step_size_lng * index)]

            tup = (temp[0], temp[1])
            l.append(tup)

    else:
        tup = (i["end_location"]['lat'], i["end_location"]['lng'])
        l.append(tup)
