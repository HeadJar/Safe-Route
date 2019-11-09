import json


def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


myO = getJSON('./ex.json')


# print(myO["routes"][0]["legs"][0]["duration"])  # duration of trip

"""
print(myO["routes"][0]["legs"][0]["steps"][0]
      ["end_location"])  # single step of trip
"""

print(myO["legs"][0]["steps"][0]["end_location"])
print(myO["legs"][0]["duration"]["text"])

time = myO["legs"][0]["duration"]["text"].split()
print(time)

print(int(time[0]))
# print(myO["legs"][0]["steps"][0]["end_location"])
