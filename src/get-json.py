import json


def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


myO = getJSON('./ex.json')


print(myO.get["routes"])
