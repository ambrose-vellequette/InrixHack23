import classes
from streetParking import findstreetpark
from crime import listcrime
from proximity import checkProximity

def combinator(lat,long):


    

    parking_array = findstreetpark(lat, long)

    crime_array= listcrime()

    newparkingarray = checkProximity(parking_array,crime_array)
    print("scores:")
    for shit in newparkingarray:
        shit.score = shit.prob*(.3*shit.prob -.7*shit.ncrime)
        print(shit.ncrime)
        print(shit.score)

    #max 3 go here
    maxscores = [0.0,0.0,0.0]
    for parray in newparkingarray:
        if parray.score > maxscores[0]:
            temp = parray.score + maxscores[1:]
        elif parray.score > maxscores[1]:
            temp = maxscores[0] + parray.score + maxscores[2]
        elif parray.score > maxscores[2]:
            temp = maxscores[0:2] + parray.score
        maxscores = temp
    print(maxscores)
            

lat = float("37.74304518280319")
long = float("-122.42438793182373")

combinator(lat,long)
