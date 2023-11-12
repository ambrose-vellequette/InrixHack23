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
rad = str(50)
#all should be strings
url = "https://api.iq.inrix.com/blocks/v3?point="+lat+"%7C"+long+"&radius="+rad

payload = {}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InN4NmYwNjBtdjAiLCJ0b2tlbiI6eyJpdiI6IjNmM2FkYWU0MWJkOTM2NmMwNTlhNzcyODdkMDI1Zjk4IiwiY29udGVudCI6IjhmODZhZTFiMWE2MmQ5YzJlMzQzN2ExZTBlODk2MTQ5YTJhMGI0ZDIzNjZmOWQ3YTRjODllZTkwMzdlNjA3ZjlmNmViM2Y3YWZmNDAyMWI1Y2VhZGRhZjUyMTdjOTA3NjFmYTVmNTM0Y2RlMjQ0MzUwZGIyYjU3Y2Y2MzRjNzUxMmZhYzYwYTc1ZTYwZjllNzg5MmQwNTQ3Mzk4NTRmODc3M2NmYzVhYmIyN2E2NGNkNzYzNWY5NzdlNjIwOTU5MzU1ZjYwZWQzMWU2YWI4NWI3ZmZlMGNlODJiZjNlZjMzZTg5NmVlMzA3ZjUzNWNhOWIyZDUwZjJkYzNhYzg5NjEyNThjMDJmMzEyMjNiZDdjOTEzOGNiMTVhNjY0MzMwMmI2ZDhhYjM1MDM4ZGZiODNhODc5ZTRiYzE5NjIzMzkyMmMxMDdhZDRkYTI1MjUzMGQxOTE3ZTRjY2RiYzE0N2E3ZmVhZjIyZjIyZmM3YTUxZmVjOTk3ZDQ5ZWU2MDBjZTI2ZWNmMzJhNzRjYzExZGM5NzE2ZTYzZDVjMDE0MzdlY2Y3ZTg1NjM4Nzk0MjVjYzdmNGQ2ZWMzZDVjYTlhM2ZkODc0NmU2ODMzZDA1NDA5MjQ4MzU4NGMxZWZiMGJjMjQ2YmYzNzRiZGJhZTFlZTMxYzU1M2ViNzYwOTljOGE1Y2NjNmNlZTdiOTdiOGJkZjY2MWFlMjJhOWExNDE4MWY3MWY3MDQ2MGM3OTU5MGQ3MGNkYjM4YjMwMTRiM2ZjNGYwY2NmY2FmNzZkZDg1ZTI0OTA3NGE1OWEzZjAwMjk2Y2JhMDk4ZDliMWIwOTZhYTQ4ZjUyMmM4ZDcwZTgzNTEzZTUwOThlNzIzYThhNzU0MDk2Mzg2In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiIzZjNhZGFlNDFiZDkzNjZjMDU5YTc3Mjg3ZDAyNWY5OCIsImNvbnRlbnQiOiJkYmFiYjY0NjIxNGNmYjgxZWI3ZTQ5MmUzNGJjMDIwMjg2OWVhYzk4MTU1NWFjNzY1NzlhZTM5NDBjZTQwMWM3ZDljNjFkMjE5YjcxMTY5OWQ3YmZmNWNiIn0sImp0aSI6ImIxN2U5M2JhLWNiY2ItNGVjOS1iYjExLTI0MzM5ZWRmNjlhYiIsImlhdCI6MTY5OTc2MDgyNSwiZXhwIjoxNjk5NzY0NDI1fQ.BQoEQzMxbo_wUQ2KRCAXfQu6O3rGPekLdx7neQX_L8g'
}

response = requests.request("GET", url, headers=headers, data=payload)
resultsList = response.json()["result"]

array = []
for res in resultsList:

    nstreet = Street(res["probability"], res["geojson"]["coordinates"][1][1], res["geojson"]["coordinates"][1][0],0)
    array.append(nstreet)
    print(nstreet.prob)

