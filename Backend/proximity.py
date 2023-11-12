import math
import classes


def checkProximity(parking_array, crime_array):
    CONV_DEG_TO_METER = float(111139)
    
    for crimes in crime_array:
        for streets in parking_array:
            # radius within ___ meters
            radius = math.sqrt(((float(crimes.lat) - float(streets.lat)) * CONV_DEG_TO_METER)**2 + ((float(crimes.long) - float(streets.long))* CONV_DEG_TO_METER)**2)
            if radius <= 100:
                streets.ncrime += 1
            
    return parking_array