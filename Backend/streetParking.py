import requests
import numpy as np
import classes
class Street:
    def __init__(self, prob, lat, long, ncrime):
        self.prob = prob
        self.lat = lat
        self.long = long
        self.ncrime = ncrime


def findstreetpark(lat, long):
  print("streetparking")
  rad = str(150)
  #all should be strings
  url = "https://api.iq.inrix.com/blocks/v3?point="+str(lat)+"%7C"+str(long)+"&radius="+rad

  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InN4NmYwNjBtdjAiLCJ0b2tlbiI6eyJpdiI6ImMzYmJiMDkxNmI2MGM0ODY2Mjc3ZTEyMTlhMmZiNzcyIiwiY29udGVudCI6IjY2ZGM4MTE1NmYyNDA4ZGRmNzMwOWM2MjFkYTY1MmU3OGEzNmI0ZjBhNmU0YTU0ZmM2NGQxZDVhMTE0ZTEyODQ0NjlhZDk3Mjc3YjkzNTI4NTk1N2UzM2YyYmQ1ZmFjOGIyNGZmNjMwODIxY2Y2YTM2YmJlZjMxOGM0YWUyYTI0ODNiNjIyMGYwYjQ3YjNhNGQyZWVmOTk3YzlhMWRkY2MxMTM2Mjk1ZWJkZjU5OTM2NmNlOWEzYTg1OGEwNzNmZjBiZTgxNGY0MDc5Y2M5ZmU2NzI5YmFkMmZhY2MwM2RmNjg0ODZjMzJhOWIzODM5MTg3YmU0N2Y5Y2NhZDg3NjU3ZDQ4MzUyMDQzNzI3MjRiNzhiNDFjZTQxZDE2MDU5MjIzYzY5YWI5ODBhZTIwYTJiOWMwODRjZGE3ZGM3MGIzOGJkMmQxNTRiNzQ2Njg3Y2YzYzUwM2Q1ZDZjZWY2ZGQyZGI1NzhkYTc5ZGQ5ODYxZmIyOWU1OWEzOWNmOTRiZjlmM2VhNzM5OTEzNWRlNTJjNWFkYzRmOWIyMzM5ODQ5NDY4MjljN2VlMTY2YmRmMmYzYTUxMWRlYmU2YWY0YmY5MGFlMDE1NTM5NjQwM2RlNmNkZGQwNmZjOWFmYzBmYTg2M2VmMDMwNDZkNTQyOWE1MzA0OTYzYjIxZDhmY2YxM2VjM2FlYTkxYWVkOTVkZDc4YjhiNDNiNmM5YzgyYmUzYmU2NjUyNGI0NTdhMWNhOTE4YWFlOWNhNTU2NzJhNzZiMDI2YjgzMjY1ZjFlMTAwNDA3N2MxNTQ3NzNkYmE2Zjg3NWY4YmQ0NmRiZGEzYTAwMWUzYzkxMjcxNWU1OTBiM2Q0MDY2MmExYWU0MjcyZTFiZTgwIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJjM2JiYjA5MTZiNjBjNDg2NjI3N2UxMjE5YTJmYjc3MiIsImNvbnRlbnQiOiIyOWY0ZTYxYzIwMmQwZGU0YzEyYmI3NTgyYjhjNDg5YjkwMjc5ZmI2YTJlZWJjNDllZTU5MjYyZDBhNmIwZjhjNjhiM2ZkMzEzZWYxMTQxYTA4NzlmMjAxIn0sImp0aSI6IjZiZDkxYjkzLTUxYTYtNGJhMC1iNzc3LWY3MGVhZmY5Mjg3MSIsImlhdCI6MTY5OTc3MTk4NSwiZXhwIjoxNjk5Nzc1NTg1fQ.tra1g73Y0UGEqVEIafA7UzTWCd-wX4N63_Q_wnQd_9Q'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  resultsList = response.json()["result"]

  parking_array = []
  for res in resultsList:

      nstreet = Street(res["probability"], res["geojson"]["coordinates"][1][1], res["geojson"]["coordinates"][1][0],0)
      parking_array.append(nstreet)
      print(str(nstreet.lat) + ", " + str(nstreet.long) +", "+ str(nstreet.ncrime))

  return parking_array

if __name__ == '__main__':
  lat = "37.74304518280319"
  long = "-122.42438793182373"

  arr = findstreetpark(lat,long)