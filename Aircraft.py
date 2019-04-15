class Aircraft:
    def __init__(self, code, flight_range, home_airport, units):
        self.code = code
        self.units = units
        self.flight_range = self.convertToMetric(flight_range)
        self.home_airport = home_airport
        
    def convertToMetric(self, flight_range):
        if self.units == "imperial":
            return round(flight_range * 1.60934, 2)
        else:
            return flight_range
        
    def getRange(self):
        return self.flight_range