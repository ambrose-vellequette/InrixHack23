import math
import classes


def checkProximity(parking_array, crime_array):
    CONV_DEG_TO_METER = 111139
    
    for crimes in crime_array:
        for streets in parking_array:
            # radius within ___ meters
            radius = math.sqrt(((crimes.lat - streets.lat) * CONV_DEG_TO_METER)^2 + ((crimes.long - streets.long)* CONV_DEG_TO_METER)^2)
            if radius < 20:
                parking_array.ncrime += 1