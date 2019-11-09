import json


def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


myO = getJSON('./example.json')


print(myO.get("routes"))
