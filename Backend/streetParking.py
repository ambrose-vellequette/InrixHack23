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


def findstreetpark(lat, long):
  print("streetparking")
  rad = str(150)
  #all should be strings
  url = "https://api.iq.inrix.com/blocks/v3?point="+str(lat)+"%7C"+str(long)+"&radius="+rad

  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InN4NmYwNjBtdjAiLCJ0b2tlbiI6eyJpdiI6IjM1YzdlOTk3ZWU1MDFmYTA4ZjA2NWUzZGY4OWM4Y2U3IiwiY29udGVudCI6ImYyY2FmMjQ0OGEzZTRiZDkyM2FmMTYwNGMxMGZiMGRjNDdkZDY2YjhmYmU5ZmQ1YTQzM2Q2NDI2OTYxODQzOThlMTQyMDdjZDY2N2M5ODA1NzY3YWVmYWZlYzQ4MTQ4MTg4YzZkMGFiOTEyMGRlYTI0NDU5ZWQ1YzgxMWU5ODFkMmI0NzQ2OTMxMDE1YjdjNDk2MDY4MjhkYTk2ZmViNjUwMGJmYTFiZmU2NDJlYjY1ZTljYTJhZGEzNTM3ZGJmZmU3ODZkOTRjMTQyMWZhM2FlMzQ1Mzk2ZDc0YzcxNzZiNGM4ZDYyMGE0MzEzNjAzYjRhYmU1M2UzMTBhZmY1Mjk2NDU3ZjRhMTZlY2M5Mjk1MTAyODFjNTcyMGNmMzE2ZWQ5OWZmMzU5OTIyZGIwMzc5MjllZmE2ZTg3NzExMzdhOTczN2Y0NjQ1Mzk2MTZmZGUwOThiNTk2MmEyNTZhZWQ5ZjFmODc1ZDQwMjJiYTFhZjE1YjM1ODZjNTFlZDI0NjQyZDZkNDE1N2FlZjM0NDE1MjYzYTQ5MmQyMmQ5NTdhN2ZiNGJjNDE4Njc0NmFjZDQ1NjBkNWZlNWRlY2FlOWQ5MTY1ZGQ1MjU2YTQ4ZTVlMTFiNWNkNThlYzU1NDMzOWQ0OGMyMzdlNmExODc1ZGZiMzcyMmU2ZGVlYzY0N2E3YWFjMWVmNDg0ZTYzMmU3YmUzYjIzN2RkNDhkZmRjZGI4NGJiYTU5MzRhZmQxZjU0OGVkY2JhODc1MjE0MGI0OGRjOGEzMTVjOTMyYTI2Nzc3OTIxYmJjYWRhODYyMDM0YzlmNzQwM2MyZWFkMmVhYzY1OTkzOTU0YjhjMDk4MmIxYjRiYTQ2YmNmNTdiOWUzODhjM2FlIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiIzNWM3ZTk5N2VlNTAxZmEwOGYwNjVlM2RmODljOGNlNyIsImNvbnRlbnQiOiJmYjg3Y2Q0MjkyMDg0YWRhM2I5NTFlM2VmZDRkYmJjNzYwZmQ2MzgwZmNjOWY1MTg3YTE0NDQyMzlhNDMwMDgzZjE2NDA2YmUxZjU2ODA3Yzc1NjFlZTkxIn0sImp0aSI6ImNjMzY2NWE0LThhZjAtNDA1NS1hZTE0LTE0N2YyNWI2NDIyMSIsImlhdCI6MTY5OTc3NjY1OSwiZXhwIjoxNjk5NzgwMjU5fQ.OOZoteIrfw1cAvV0AwqTHc6OKFgHFKKQnzNycEvsWuM'
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