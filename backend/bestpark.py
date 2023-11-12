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
#        if shit.prob == 0:
#            probability = .01
#        else:
#            probability  = shit.prob
        probability = float(shit.prob) if shit.prob is not None else 0.0
        shit.score = float(probability)*(.003*float(probability) -.7*shit.ncrime)
        print(shit.ncrime)
        print(shit.score)


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
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InN4NmYwNjBtdjAiLCJ0b2tlbiI6eyJpdiI6Ijk2NmI0YWM1ZjE2MThiNjJlMzczYjFjMmRhMDMyYzYxIiwiY29udGVudCI6IjJmYzI1ZmI2MmU5Njk5NGFmNjYxMGJlM2RjMmRhZjg1NTQ2MDA3MmY0MTQzMzMxMjYxNDExYzk3MThlOWMxNDg1ZWJhYjliOGJiMDZjMzFlYzlhMTY5OGMyZjhiZmQxNGI0Y2VkOTk4OWM4MmIxZjE1ZmQ0NmVkZmM2YTNlNzVlZGQzZDIyMmI4Yjk2ZjkyNzQ3MDliM2ZkYmRjN2JiZjIxZDQ1ZjRmY2FhM2VjMTBkNmUzZmU3YTliOGVhYTViNmY5N2Y4OGJkMzU1OTEwODU3ZDM0OTI5YWE3MWU1ZDQ5ZGY5ODAyMTFjZjcwN2E3NTIwNjExYjA5MTJkNGRmZGI0MWQxNjQ1MWFjMTUyOGY4MmQzZWE4MzMwZGM2MzAwY2I0MDkwZGQ3MDA2NzA3Yzc2Y2RlMzVjNGVkOGE0YjU1NzY3MDI0M2ZmYjM5NzI5M2M0ODMxYjI3ZWYzMzVhNGQxZDRiZjlhMzhkYzkxZjQzOTM1MGYyZGM3Yjg2OWZlN2VkOTE3NWZjYWUxNzJiOGIyMTRlZmNhM2RhMzdiYTQzYWE4Y2VlY2UzMDlkMjYxMDI0NGViNWZlNTU5ZDQ1ZGYyZDBkNWU1NmEwZWMxY2NkZjMwN2I0NTMzNWU3OTI4NzdlOGI5YTEwNjg4YmMyZDdiNTk1NzlmZWVhMzQyZDlkY2U4YTE3OWUzOTI5YTg2NzViOTBlZjk4YzYwYzY2NjFhYWFkNTYxZGFkNGMzNTJlMGM4OTgxYWUyOTJjYzI2ZTJhOTAyNzg2NmRkMzFjZmViNTVhZmUwMTczZWVmYjg2N2ViM2MzZWYxZWU0NmNmMTRhZDViYzQyMGIzMGFlYjgyMGJiOWU3ZTg5Y2ZiZmQ4YTE2MDEzIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI5NjZiNGFjNWYxNjE4YjYyZTM3M2IxYzJkYTAzMmM2MSIsImNvbnRlbnQiOiIzOGVhMjdiNjJiOTk5NTFhZWE2NjI4ZGZjNTMxZGZmNzRiNzg3ZjNhNGUwNzE2NTM2ZTVhMWVmNjA3ZTZlOTY1Nzk5N2JjZDVhNTE3ZmIwMjhiZjY1NmIyIn0sImp0aSI6ImNhZTM4NmU5LWYzMjktNDQ4My1iYzg1LWM2ZDIzNjE4MTQ4ZCIsImlhdCI6MTY5OTc4NDIyNywiZXhwIjoxNjk5Nzg3ODI3fQ.vnLeei68TxTz3AOg6UX041Q_vVZ4-vhYMyDuQ8y4hfA"
    a = combinator(lat,long,token)
