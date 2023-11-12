import requests
import classes

class Crime:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
def listcrime():
    print("listcrime")
    url = "https://data.sfgov.org/resource/tmnf-yvry.json?category=VEHICLE THEFT"
    payload = {}
    headers = {
    'crime': '57jx9amcitpjm6bxd2psltklu	'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resultsList = response.json()
    crimes = 0
    crime_array = []
    for res in resultsList:

        newcrime = Crime(res["y"], res["x"])
        crime_array.append(newcrime)
        #print(newcrime.lat +", "+ newcrime.long)
        crimes += 1
    #print(crimes)
    return crime_array

if __name__ == '__main__':
    arr = listcrime()