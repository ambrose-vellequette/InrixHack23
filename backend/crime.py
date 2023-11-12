import requests

class Crime:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

url = "https://data.sfgov.org/resource/tmnf-yvry.json?category=VEHICLE THEFT"

payload = {}
headers = {
  'crime': '57jx9amcitpjm6bxd2psltklu	'
}

response = requests.request("GET", url, headers=headers, data=payload)
resultsList = response.json()

array = []
for res in resultsList:

    newcrime = Crime(res["y"], res["x"])
    array.append(newcrime)
    print(newcrime.lat +", "+ newcrime.long)
