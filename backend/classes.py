import requests

class Street:
    def __init__(self, prob, lat, long, ncrime,score):
        self.prob = prob
        self.lat = lat
        self.long = long
        self.ncrime = ncrime
        self.score = score

class Crime:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long