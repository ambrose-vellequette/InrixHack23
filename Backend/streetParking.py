import requests

url = "https://api.iq.inrix.com/blocks/v3?point=37.74304518280319%7C-122.42438793182373&radius=50"

payload = {}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InN4NmYwNjBtdjAiLCJ0b2tlbiI6eyJpdiI6ImFkMDQxYzVlYTY5YzI2OTgyMGQ2MjYzYmU5NGEzODBlIiwiY29udGVudCI6IjM3ZTdjMjg3N2I2MTkzNTI1YTU1YzE4MjlkZGViNWU3MjE0NDhhMzkzYzdlZTllYmM4OGVlNjYwOTY5YWM0MTgxNDE4M2M3YjRhZTUwNDNiYWRlNDBkYzEyOWM0ZjAxMjBhNzc4OWE0ZjQ3ZjMyZWEzNjVmYWEyZjIxYmVjY2U0ZjU4N2UyZDMzZWY3Zjc5YTU4N2ZmZDkzYjVjNjcyYmQwMTQ4MzhkOTBiZDUwZTVhMGY5OWRiOTI2YmFjNzU2NzhkNWMxNmFkOTAyNTdhMWU4YjA5ZmVkNjM0YzAzYzM3MzhhZmVmNmYyNzMyMmQ4ZmQ2ZTZiNmY5N2U4NGZmNGIyM2JiYTVmYmZhZDcxYjBlM2IzMjE1ZjM5ODM0YWI0YWYyYjAxODcwMWE3YTgyNDM5MTVlNmYyZDlhZjY3ZTg3MmFhMTVjNDUxYmYyNGZhYzM4MTRiYTJlNDJlNWU1N2E3N2Y5MTBlYjA3YmY1MWEzZmE4NmRjNmIxZTE3Y2I2ZTM1NTE2MjFkMWRiMjNhNmQ0ZTQ4Y2ZmMTg2ZmQ1MTY3YTViOWQxYjQ3ZDcwZTNiZjU2ZmNiY2M1OTk3ZmIwNTU2ZTZiOGE5MmRjZDFhOWExYjg4MDM5Y2FhNmRmZmQ0YTI4ZmViZmM3OThiY2IxMWNmODdkMjQ1Mzg0ZGYyMzVkYmU1YzFiZGZiNGFiOTc0NWQ2M2MyOTRkYTRhZjU0NTFlOTE4NGJjNmQxNjE0ZTU2Y2U1N2Q1ZmRjMjc0MjEyOGMzNjljOTg4YzNjMGYwZjNhNWEwNjNkYTI5MzgyYjQ1ZWE2ZDYyZmY4N2QyYjdhNzJiMWIyNDJmMTU3M2RhYzljNmI0ZjQ5ZjJkNTQ1MzQ3ODkwYmY2In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJhZDA0MWM1ZWE2OWMyNjk4MjBkNjI2M2JlOTRhMzgwZSIsImNvbnRlbnQiOiI2YmYzZjJiNjUyNzFhNzZmNWM3ZWUwYTJmOWY3YWM4NDM1NTk5YTJiMjc0MWQyODZlOWJmYzkzNDkxYmZmOTZhMTYxODFhNzQyOWU1M2M1YmY3YzI3ZGZmIn0sImp0aSI6IjFhOGRlMzg1LTM0NDItNDlhNy04N2VmLTBlNDIxZGJkZmE0OSIsImlhdCI6MTY5OTc0NjEyNCwiZXhwIjoxNjk5NzQ5NzI0fQ.rEVxppE8bLCodyiis4cAMj4rQzvPKNaSY1nS73FRYAc'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
