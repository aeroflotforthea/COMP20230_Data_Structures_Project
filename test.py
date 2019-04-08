import math


class Airport:
    
    def __init__(self, name, longitude, latitude, exchange_rate):
        self.__name = name
        self.longitude = longitude
        self.latitude = latitude
        self.__exchange_rate = exchange_rate
        
    def getExchangeRate(self):
        return self.__exchange_rate
    
    def getName(self):
        return self.__name
    
    def setExchangeRate(self, new_exchange_rate):
        self.__exchange_rate = new_exchange_rate
        print("Exchange rate set to ", new_exchange_rate)
        return self.getExchangeRate()

airport = Airport("LHR", "101", "102", 1.34)

airport.getExchangeRate()

# airport.setExchangeRate(1.55)

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
        
plane = Aircraft("737", 5600, "LHR", "imperial")


class Route:
    
    def __init__(self):
        self.__destinations = []
        # it would make sense for destinations to be a circular array
        self._next = None
        self._current = None
        self._previous = None
        # this sequence has been produced the graph. The graph will go through each airport and will build a route
        self.__total_score = 0
        self._list_of_scores = []
        
        
    def set_destinations(self, destinations):
        self.__destinations = destinations

    def append_to_route(self, airport):
        self.__destinations.append(airport)

    def calculate_score(self):
        self._previous = self.__destinations[0]
        # set the first airport to previous and current
        for i in range(len(self.__destinations)):
            self._current = self.__destinations[i]
            try:
                self._next = self.__destinations[i + 1]
            except:
                self._next = self.__destinations[0]
            distance = self.calculate_distance(self._current, self._next)
            current_score = self._current.getExchangeRate() * distance
            self._list_of_scores.append(current_score)
            # self._previous = self._current
            # self._current = self._next
            
            
    def calculate_distance(start_airport, end_airport):
        latitude1 = start_airport.latitude
        longitude1 = start_airport.longitude
        latitude2 = end_airport.latitude
        longitude2 = end_airport.longitude

        # The following formulas assume that angles are expressed in radians.
        # So convert to radians.

        latitude1 = math.radians(latitude1)
        longitude1 = math.radians(longitude1)
        latitude2 = math.radians(latitude2)
        longitude2 = math.radians(longitude2)

        # Compute using the law of cosines.

        # Great circle distance in radians
        angle1 = math.acos(math.sin(latitude1) * math.sin(latitude2) \
                 + math.cos(latitude1) * math.cos(latitude2) * math.cos(longitude1 - longitude2))

        # Convert back to degrees.
        angle1 = math.degrees(angle1)

        # Each degree on a great circle of Earth is 60 nautical miles.
        distance1 = 60.0 * angle1
            
        in_kilometres = distance1 * 1.852
        
        return in_kilometres

    def get_destinations(self):
        return self.__destinations
    
    def getScores(self):
        return self._list_of_scores
    
    
madrid = Airport("Madrid", 3.7038, 40.4168, 0.84)
london = Airport("London", 0.1278, 51.5074, 1.17)
dublin = Airport("Dublin", 6.2603, 53.3498, 1)
berlin = Airport("Berlin", 13.4050, 13.4050, 1.99)


def buildGraph(list_of_airport_objects, airplane_object):
    # first thing: build the graph object
    my_graph = {}

    for airport in list_of_airport_objects:
        my_graph[airport.getName()] = []
    
    for airport in list_of_airport_objects:
        for i in range(len(list_of_airport_objects)):
            if list_of_airport_objects[i] != airport:
                print("they're not the same!")
                if Route.calculate_distance(list_of_airport_objects[i], airport) <= airplane_object.getRange():
                    my_graph[list_of_airport_objects[i].getName()].append(airport.getName())
        
    
    print(my_graph)
    
buildGraph([madrid, london, dublin, berlin], plane)