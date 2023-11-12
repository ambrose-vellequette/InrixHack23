import requests

url = "https://data.sfgov.org/resource/tmnf-yvry.json?category=VEHICLE THEFT"

payload = {}
headers = {
  'crime': '57jx9amcitpjm6bxd2psltklu	'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

