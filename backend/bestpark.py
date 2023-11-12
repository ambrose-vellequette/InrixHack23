import classes
from streetParking import findstreetpark
from crime import listcrime
from proximity import checkProximity

def combinator(lat,long,token):


    

    parking_array = findstreetpark(lat, long,token)

    crime_array= listcrime()

    newparkingarray = checkProximity(parking_array,crime_array)

    print("scores:")

    for shit in newparkingarray:
        shit.score = shit.prob*(.003*shit.prob -.7*shit.ncrime)
        print(shit.ncrime)
        print(shit.score)


    #max 3 go here
    maxscores = [newparkingarray[0],newparkingarray[1],newparkingarray[2]]
    print(maxscores)
    temp = maxscores
    for parray in newparkingarray[3:]:
        if parray.score > maxscores[0].score:
            temp = [parray, maxscores[0], maxscores[1]]
        elif parray.score > maxscores[1].score:
            temp = [maxscores[0],parray,maxscores[1]]
        elif parray.score > maxscores[2].score:
            temp = [maxscores[0],maxscores[1],parray]
        maxscores = temp
        print(maxscores[0].score, maxscores[1].score, maxscores[2].score)
    
    
    dictionary = {
        "lat1": maxscores[0].lat,
        "long1": maxscores[0].long,
        "lat2": maxscores[1].lat,
        "long2": maxscores[1].long,
        "lat3": maxscores[2].lat,
        "long3": maxscores[2].long,
    }
    print(dictionary)
    return dictionary
            
if __name__ == '__main__':
    lat = float("37.74304518280319")
    long = float("-122.42438793182373")
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InN4NmYwNjBtdjAiLCJ0b2tlbiI6eyJpdiI6ImVmNTc5YmVhNDg4YjNhNWJkNzJlZjllZTFlNGFlYjhkIiwiY29udGVudCI6IjkyMTRkZDM4MzEzNDk5YjQ5NWZmMWEwNGU0OGNiZGZhYzFjZDU3N2U2NWM5NmIxMTVmZDE2ZjAwODBhMjdiNzQwYjFhOTUxMzQ2NTRkNDdlNDlhZWI3ZDA1MWMyMTM3MzdmZDI2NTIwODBiMDA4YTQxZmE0YTA4NjZkOGMyNGYxNTg4ZmFjOTM5NWZkODNmNWJiM2ExNDcxOTIxOWEyNWM1OTkxYmQ0NWU0N2E3YzFlZWE1YjlhM2I3OGY4MmQ5ODVjMjQ5YjNjZjFiYzhiZmZlMWMzNzJiOWZhZmRiMjRkYWRlYzIzOWRlNzMxOGQ2NmUxNzdhMGRkNmQwNTU0OTRiYmFkMjQ4MDJmMTY2OWIxNWRmN2VhMWIyNTg0MDY1YzcxZTM4OGI0NTQzYzlhZjM1YjhkN2IyYzVlNzM5MGRiNzlhZjFiMDNkMjhkN2FhMmQ0NDllY2ZhZDRkYWYzNTRmOTVkZjI0Y2Q1NDAyYTk2NWU4N2VlMjRlM2E3ZTYyODUzMWQ5YmM4YWNhYTIyNjVjZjQxZDU1ZTk1Yzg0Mzk0ZGIyMDQ1MTA0OGI1ODY5NWY3NmYyYzg2Nzk2MGRlZjRkN2NhN2IyMmJiMjgzZWVhMjgxOThhMTk1MmQxZGYzZGU1OGNhMDVlOGJlNmE3ZjcxMzkwZTJkNDE2NjVhNjQzMzYzM2NiNWY5YmUwNTEzYTZmMzEwNWQyNDFkODYxZjlhNjk3YTllMWI4NjUwZDgzMmQ1MTJmNDQyYjUxYzQ0OWE5MWE5NjMwZDg5MDM5YjQxN2ZiMTNkYzk0NGUyZDQ4NTlhMThkYjQyM2NmM2QzMTVmNzY2YTI4MWE5NGNhNzRhOGNiZGI0M2QyMDU4ZjBkMjVkOWFlIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJlZjU3OWJlYTQ4OGIzYTViZDcyZWY5ZWUxZTRhZWI4ZCIsImNvbnRlbnQiOiJiZDVmYzA2MTE2MzFiY2I4YWNjZjI2N2NkN2I5YzJhY2Q1YzU0ZDY5NTY5NzVkNjk3ZGY0NTY1YmI4OGU3YjE5MjkyZmFlNDIxYzdhOWM1YzE3ZjQ5Y2VlIn0sImp0aSI6Ijk5MmI3OTE5LWVkYWUtNDc2Ny05YjA2LWQ1Yzg4OGYzNDVhNyIsImlhdCI6MTY5OTc4MDMyNiwiZXhwIjoxNjk5NzgzOTI2fQ.Mi_SwWrEER6J1OIYtDoFbixGJ1JoCT-TCIC5e_Lg0w4"
    a = combinator(lat,long,token)
