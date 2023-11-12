from math import radians, sin, cos, sqrt, atan2
import classes

"""
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

    
    distance = haversine(parking_array[0].lat,crime_array[0].lat,parking_array[0].long,crime_array[0].long,)

    if distance <= 1000:
        streets.ncrime += 1

    print(streets.ncrime)
    return parking_array
def haversine(lat1, lat2, lon1, lon2):
        crime_array[0].lat
        dlat = float(lat2) - float(lat1)
        dlon = float(lon2) - float(lon1)
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        radius = 6371000 


        distance = radius * c
        
        return distance
"""

def haversine(lat1, lon1, lat2, lon2):

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Radius of the Earth in meters (mean value)
    radius = 6371000  # meters

    # Calculate the distance
    distance = radius * c

    return distance

def are_coordinates_within_distance(lat1, lon1, lat2, lon2, max_distance=20):
    distance = haversine(lat1, lon1, lat2, lon2)
    return distance <= max_distance


def checkProximity(parking_array, crime_array):
    for crimes in crime_array:
        for streets in parking_array:
            if are_coordinates_within_distance(float(streets.lat), float(streets.long), float(crimes.lat), float(crimes.long), 20):
                streets.ncrimes += 1
            print(streets.ncrimes)

    return parking_array