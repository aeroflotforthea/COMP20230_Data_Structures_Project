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

    def calculate_score(start_airport, end_airport):
        distance = Route.calculate_distance(start_airport, end_airport)
        return start_airport.getExchangeRate() * distance
           
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



plane = Aircraft("737", 5600, "LHR", "imperial")

madrid = Airport("Madrid", 3.7038, 40.4168, 0.84)
london = Airport("London", 0.1278, 51.5074, 1.17)
moscow = Airport("Moscow", 37.618423, 55.7558, 0.5)
shanghai = Airport("Shanghai", 121.4737, 31.2304, 0.4) 
paris = Airport("Paris", 2.3522 , 48.864716, 1)
hk = Airport("Hong Kong", 114.149139, 22.286394, 0.3)
athens = Airport("Athens", 23.727539, 37.983810, 1)
la = Airport("Los Angeles", -118.243683, 34.052235, 1.5)
hawaii = Airport("Honolulu", -157.917480, 21.289373, 1.5)
NYC = Airport("New York", -73.935242, 40.730610, 1.5)
dublin = Airport("Dublin", -6.266155, 53.350140, 1)



def firstcost(home, graph, start, flightlist, routes, path =[],a=0, cost=0): 
    path = path + [start]
    cost+=a
    all_there = True
    for item in flightlist:
        if item not in path:
            all_there = False
            break

    if all_there:
        if home in graph[start]:
            path.append(home)
            start_string = start_string = start +":" + home
            a = routes[start][start_string]
            cost += a
            return path, cost
    else: 
        furthest = 0
        for node in graph[start]:
            node_key = start +":" + node
            if routes[start][node_key] > furthest:
                furthest = routes[start][node_key] 
                special_node = node
        firstcost(home, graph, special_node, flightlist, routes, path, a, cost)
            

                
    for node in graph[start]: 
        if node not in path: 
            start_string = start +":" + node
            a = routes[start][start_string]
            newpath = firstcost(home, graph, node, flightlist, routes, path,a, cost) 
            if newpath:  
                return newpath 
    return None

def build_flight_possibilities(list_of_airports, possibilities_lookup, plane):
    for i in range(len(list_of_airports)):
        possibilities_lookup[list_of_airports[i].getName()] = {}
        for j in range(len(list_of_airports)):
            if i != j and Route.calculate_distance(list_of_airports[i], list_of_airports[j]) <= plane.getRange():
                possibilities_lookup[list_of_airports[i].getName()][list_of_airports[j].getName()] = list_of_airports[j]

    return possibilities_lookup

list_of_airports = [paris, dublin, london, NYC, hk, hawaii, shanghai]

possibilities = build_flight_possibilities(list_of_airports, {}, plane)


def buildRouteCosts(list_of_airports):
    costs = {}

    for airport in list_of_airports: 
        costs[airport.getName()] = {}
        get_costs_from = possibilities[airport.getName()]
        for key in get_costs_from: 
            costs_key = airport.getName() + ":" + key
            costs[airport.getName()][costs_key] = Route.calculate_score(airport, possibilities[airport.getName()][key])

    return costs

routes = buildRouteCosts(list_of_airports)


my_list = []

for airport in list_of_airports:
    my_list.append(airport.getName())

firstroute, bestcost = firstcost("Dublin", possibilities, "Dublin", my_list, routes)

print(bestcost)