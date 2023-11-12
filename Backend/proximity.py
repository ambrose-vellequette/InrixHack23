import math
import classes


def checkProximity(parking_array, crime_array):
    #  from Haversine
    lat_mid = abs(float(crime_array[0].lat) + float(parking_array[0].lat) / 2)
    CONV_LAT_TO_METER = 111132.954 - 559.822* math.cos(2.0 * lat_mid) + 1.175* math.cos(4*lat_mid)
    CONV_LONG_TO_METER = 111132.954 * 6367449 * math.cos(lat_mid)
    
    for crimes in crime_array:
        for streets in parking_array:
            # radius within ___ meters
            lat_dist = (float(crimes.lat) - float(streets.lat)) * CONV_LAT_TO_METER
            long_dist = (float(crimes.long) - float(streets.long)) * CONV_LONG_TO_METER

            radius = math.sqrt((lat_dist)**2 + (long_dist)**2)
            if radius <= 100000:
                streets.ncrime += 1
                
            print(streets.ncrime)
    return parking_array