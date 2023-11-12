import classes
from streetParking import findstreetpark
from crime import listcrime
from proximity import checkProximity

def combinator(lat,long):


    

    parking_array = findstreetpark(lat, long)

    crime_array= listcrime()

    checkProximity(parking_array,crime_array)
    print("scores:")
    for shit in parking_array:
        shit.score = shit.prob*(.3*shit.prob -.7*shit.ncrime)
        print(shit.ncrime)
        print(shit.score)
    
    #max 3 go here


lat = float("37.74304518280319")
long = float("-122.42438793182373")

combinator(lat,long)
