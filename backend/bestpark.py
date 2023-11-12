import classes
from streetParking import findstreetpark
from crime import listcrime
from proximity import checkProximity

def combinator(lat,long,token):


    

    parking_array = findstreetpark(lat, long,token)

    crime_array= listcrime()

    newparkingarray = checkProximity(parking_array,crime_array)

    #print("scores:")

    for segs in newparkingarray:
#        if shit.prob == 0:
#            probability = .01
#        else:
#            probability  = shit.prob
        probability = float(segs.prob) if segs.prob is not None else 0.0
        segs.score = float(probability)*(.003*float(probability) -.7*segs.ncrime)
        #print(segs.ncrime)
        #print(segs.score)


    #max 3 go here
    value1 = newparkingarray[0]
    value2 = newparkingarray[1]
    value3 = newparkingarray[2]
    if value1.score >= value2.score and value1.score >= value3.score:
        highest = value1
        if value2.score >= value3.score:
            middle = value2
            lowest = value3
        else:
            middle = value3
            lowest = value2
    elif value2.score >= value1.score and value2.score >= value3.score:
        highest = value2
        if value1.score >= value3.score:
            middle = value1
            lowest = value3
        else:
            middle = value3
            lowest = value1
    else:
        highest = value3
        if value1.score >= value2.score:
            middle = value1
            lowest = value2

        else:
            middle = value2
            lowest = value1

    maxscores = [highest, middle, lowest]
    #print(maxscores)
    temp = maxscores
    for parray in newparkingarray[3:]:
        if parray.score > maxscores[0].score:
            temp = [parray, maxscores[0], maxscores[1]]
        elif parray.score > maxscores[1].score:
            temp = [maxscores[0],parray,maxscores[1]]
        elif parray.score > maxscores[2].score:
            temp = [maxscores[0],maxscores[1],parray]
        maxscores = temp
        #print(maxscores[0].score, maxscores[1].score, maxscores[2].score)
    
    
    dictionary = {
        "lat1": str(maxscores[0].lat),
        "long1": str(maxscores[0].long),
        "lat2": str(maxscores[1].lat),
        "long2": str(maxscores[1].long),
        "lat3": str(maxscores[2].lat),
        "long3": str(maxscores[2].long),
    }
    print(dictionary)
    return dictionary
            
if __name__ == '__main__':
    lat = float("37.74304518280319")
    long = float("-122.42438793182373")
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InN4NmYwNjBtdjAiLCJ0b2tlbiI6eyJpdiI6IjA1ZDgxNDg5MzVlN2FkZmEzMjFmZDlkODJmNjJhZmNlIiwiY29udGVudCI6ImU3ZjlmZjc3ZWRhZTRlYjkxMjAyMjhmZTVjNDIzYTAzMmRiNjA5ZmU3OWExOTI1YjRjYzgxYjFkMzQzMTNlM2MzZWJkZGQ2NmQ1MGFkYTBhYmFmOGE0YTY3MTNjNjViNzYxMTIyNjI2NGUxMzA4NzNhODY5ZGE2N2UyNDA3NTU2OTNlMzNlYWU4YjU1YjcxMGFkMDEyMGZkYjVkZWY3ZjYzYmU1MWJkMTA5ZWY3YmQyNzk2YzQxMTljZmMxZjI4ZWU2ZWE1NzE1Njc5ZDgyYzdhMDYwMjlmMDJkMjdmZGE4YTI3NzE2MmY2NzdiYzk0OTAxNTU2ZTAyM2IzYmEzNDU1ZjZjOThiODAzNjE1ODc4NjI3MWY2YmQ3MWFhYzQyNzNkODViYWZmMDE4MDBkOGRiMmVlOTU5MzZkNzViZTQyMGU2MmQyNGE3NzNiMGIxM2U5MjU1Y2I0ZWI4YzI0OWJmZTQzNmZkZmMyNWUyNDFjNjAwYWYzM2YxMmYxY2U1MTM3ODJhNmJmYzkzNTNhZGRhOWFmOWIxZGE4ZDQxYzIzZGM0ZTZlYzRhODQ5Mzk5NWZmMjQ5Y2JiMTdjN2IzOWRlMzk1ZWM0MTNiZDM4ZWRlZDkwMmYxMzAwNGQyNmVkOGU1NjM2YjQwMTIzMDdiN2MwMGIwMWJiZjg4OTI4MTM0YWFiMDk2OTQyZjE1MDBhNDRkYWM4ZWEyN2RlOWQ0ZGIzZWRlMTc5NTVlMDA2YTdiMTI3MjYyNmJkZTg5ZGEzZmMwMjUzMTZmNGMzMWQ5MGQ3NjJlZmNhNjhmOWMyZjAzMDRkYjQzNzE0OTExNTdlZDVjNDg2YWM1ZWVjMmRkNzgwNTRjMTVkNmJhOWRhYTU3ZGJhNjYwIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiIwNWQ4MTQ4OTM1ZTdhZGZhMzIxZmQ5ZDgyZjYyYWZjZSIsImNvbnRlbnQiOiJiMGQ4ZjM3M2UxYWE2OGUyNmYzYTBhYzM0MTUwNDM1ZDJiYjczOWM1NjE4N2E3MTc1YWRjMDM0ZjI0Mzk3ZDI3MmU4N2NmMWFiYTFhZTIzOTgyZDBiOTk4In0sImp0aSI6ImQ1MDMyZDRkLTZjZTAtNDE5MS1iNTZkLWZmNWI5NTU1NDI3YiIsImlhdCI6MTY5OTgwMzkyNywiZXhwIjoxNjk5ODA3NTI3fQ.8hdSylBW8wi2Qfi3b3nkWcbvP6-pGiS4LVY83fE7op0"
    a = combinator(lat,long,token)
