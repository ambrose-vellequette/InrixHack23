import requests
import numpy as np

class Street:
    def __init__(self, prob, lat, long, ncrime):
        self.prob = prob
        self.lat = lat
        self.long = long
        self.ncrime = ncrime

lat = "37.74304518280319"
long = "-122.42438793182373"

def findstreetpark(lat, long):
      
  rad = str(50)
  #all should be strings
  url = "https://api.iq.inrix.com/blocks/v3?point="+lat+"%7C"+long+"&radius="+rad

  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InN4NmYwNjBtdjAiLCJ0b2tlbiI6eyJpdiI6ImJiOWE1MjFkY2YzZjE4YzRmOTAwZGEzYjNiMTZmMjc2IiwiY29udGVudCI6ImY2YzUwZjVkM2MzNWFlYTdmMDhhYTJmZDYwZTRlNTZmNDcyODhhYzRjMzM3MWZmYjU1MDA1NWZlZmJmZjAyNTE4NTEzMzU4OTViYTc0YjkyM2U0ZTI0ZjQ1NzlhY2FjZTMwY2U5YTc0YmNjNTFjM2FhMTQ4ZTY2YWJlNzQ1MDU1NDQxZDZlMmFlYjY1MTMyYmE1YjlkNjcxZGFjN2UxYjIwYmU3OTQ4NzMxZDM4YzMxYjUyYzlkY2M1MzM2NDczMDY4MDU4YjVjMzc4YWRhMWNlYTRmNDg2NmRlMDM2ZDIwMmU3ZGEwNzliY2ZjOTNkYjVhNGUwMGQ4YzQ4NGRhZmRjNjc5MTJhYzdiNTBhYjI5MTQyMjA1NTRhZDliMmQ1MjVkNjFhYjU2ZjZlMTE1Mjk1NzhjYmNkOTY2YTFlYzZhM2ZhNmQzYzZiYWQ5NzUxNmMwOTM4Mzg1NDlmMTlhYjJjMGRlNDczN2RlMDFiY2M3NjFlZmI2YWI2MDgxZDBjNjI1YzQ3Mjc3NTAxNjk2NGY3ODM4MzM4MDA4NmQzZjRkNzY4ZGI4YjhkY2UwZmNlOGUyNTAxOWJjMzU2MTRhNjMzMjI5ZjZmM2NkMjQ4OTZlNzA0ZWJhZGQ1MzEyNjBlN2Q2ZWZmZTYxN2Y4MTFlNDFlY2U1ZTI2ODhhZmVkZTNjMmZhYTQ0MzFjZmI5YjY2NTNlMDczNTg2ZGUxMDRkYzY1MTRiNmE4MjE5M2NmZjk1MTYxOWRjYjFhNjUxYmFhZDliNDYzYTE0ODcxNTNhOGE5YTgwMmNiNTM4M2YwN2YwNjE4ZjEzYjNlZmY1NDBkMmYzNTg2N2NkOWQwZWZjY2U4Y2Y4YTY3ZDY5MmYwNDE0OTc2MzQ4In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJiYjlhNTIxZGNmM2YxOGM0ZjkwMGRhM2IzYjE2ZjI3NiIsImNvbnRlbnQiOiJlNDg0MjA2ZDNiNThhYmFmYzZhNmE3ZDg3ZGQwZWExYjc5MDJiNmNmYTAzNTE5ZjkwMDMzNTJhZmZmZDYwMTIzOGE2NDFkZTMzYmE1NjViZDEyNmMzNWNhIn0sImp0aSI6ImI3MzRjMGExLTg3MWEtNDRiYS1hMWQxLTkyOTQ2Mzc0MmY3MSIsImlhdCI6MTY5OTc2NzA3MSwiZXhwIjoxNjk5NzcwNjcxfQ.Dkx6mIWHj73vcq0wdPNTrqa57JYCSXyK_auKAnBHVI4'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  resultsList = response.json()["result"]

  parking_array = []
  for res in resultsList:

      nstreet = Street(res["probability"], res["geojson"]["coordinates"][1][1], res["geojson"]["coordinates"][1][0],0)
      parking_array.append(nstreet)
      print(str(nstreet.lat) + ", " + str(nstreet.long))

  return parking_array
