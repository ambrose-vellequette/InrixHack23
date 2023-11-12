from math import radians, sin, cos, sqrt, atan2
import classes



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

def are_coordinates_within_distance(lat1, lon1, lat2, lon2, max_distance):
    distance = haversine(lat1, lon1, lat2, lon2)
    return distance <= max_distance


def checkProximity(parking_array, crime_array):
    for crimes in crime_array:
        for streets in parking_array:
            if are_coordinates_within_distance(float(streets.lat), float(streets.long), float(crimes.lat), float(crimes.long), 250):
                streets.ncrime += 1
            #print(streets.ncrime)

    return parking_array