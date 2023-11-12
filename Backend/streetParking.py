import requests
import numpy as np
import classes
class Street:
    def __init__(self, prob, lat, long, ncrime,score):
        self.prob = prob
        self.lat = lat
        self.long = long
        self.ncrime = ncrime
        self.score = score


def findstreetpark(lat, long,token):
  print("streetparking")
  rad = str(400)
  #all should be strings
  url = "https://api.iq.inrix.com/blocks/v3?point="+str(lat)+"%7C"+str(long)+"&radius="+rad

  payload = {}
  headers = {
    'Authorization': 'Bearer' + token
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  resultsList = response.json()["result"]

  parking_array = []
  for res in resultsList:

      nstreet = Street(res["probability"], res["geojson"]["coordinates"][1][1], res["geojson"]["coordinates"][1][0],0,0)
      parking_array.append(nstreet)
      print(str(nstreet.lat) + ", " + str(nstreet.long) +", "+ str(nstreet.ncrime))

  return parking_array

if __name__ == '__main__':
  lat = "37.74304518280319"
  long = "-122.42438793182373"

  arr = findstreetpark(lat,long)