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

    a = combinator(lat,long)
