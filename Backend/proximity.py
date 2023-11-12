


def checkProximity(parking_array, crime_array):
    for crimes in crime_array:
        if parking_array.lat - crime_array.lat > -20 &  parking_array.lat - crime_array.lat < 20:
            if parking_array.long - crime_array.lat > -20 & parking_array.long - crime_array.long < 20:
                num_crimes + 1

    return num_crimes