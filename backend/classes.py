import requests

class Street:
    def __init__(self, prob, lat, long, ncrime):
        self.prob = prob
        self.lat = lat
        self.long = long
        self.ncrime = ncrime

class Crime:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long