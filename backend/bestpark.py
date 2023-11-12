import classes
from streetParking import findstreetpark
from crime import crimelist
from proximity import checkProximity

def combinator(lat,long):

    parking_array = findstreetpark(lat, long)

    crime_array= crimelist()

    checkProximity(parking_array,crime_array)
    
    for shit in parking_array:
        shit.score = shit.prob*(.3*shit.prob -.7*shit.ncrime)
    
