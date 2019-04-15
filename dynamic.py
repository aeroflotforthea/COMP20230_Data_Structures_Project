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
    
    
madrid = Airport("Madrid", 3.7038, 40.4168, 0.84)
london = Airport("London", 0.1278, 51.5074, 1.17)
dublin = Airport("Dublin", 6.2603, 53.3498, 1)
berlin = Airport("Berlin", 13.4050, 13.4050, 1.99) 

# print(Route.calculate_distance(london, london))

def buildGraph(list_of_airport_objects, airplane_object):
    # first thing: build the graph object
    my_graph = {}

    for airport in list_of_airport_objects:
        my_graph[airport.getName()] = {}
    
    # each airport is a key to a dictionary
    for airport in list_of_airport_objects:

        # this will go through madrid, dublin, etc. 

        for i in range(len(list_of_airport_objects)):
            print(airport)
            print(list_of_airport_objects[i])
            distance = 0
            if list_of_airport_objects[i] == airport:
                distance = 0
            else: 
                distance = Route.calculate_distance(list_of_airport_objects[i], airport)

            if distance <= airplane_object.getRange():
                my_graph[airport.getName()][list_of_airport_objects[i].getName()] = list_of_airport_objects[i]

                    
    return my_graph








# my_graph = buildGraph([madrid, london, dublin, berlin], plane)

# print(my_graph)


# '''
# createLowestPrice takes in:

# start_airport # this is the airport we have to start at and return to

# graph # this is our list of airports that we have to traverse to

# current_airport # this is the airport that either will, or won't be included in the route

# big_cost # this is the overall cost of the route thus far. We continue to add to this, 
# UNLESS all of the airports have been visited

# # a dictionary, mem, that stores the big_cost

# ''' 





def master():
    my_graph = buildGraph([madrid, london, dublin, berlin], plane)
    for key in my_graph:
        print(key)
        print(my_graph[key])
    createLowestPrice("Dublin", len(my_graph)-1, len(my_graph)-1, my_graph, 0, {}, [])

# '''

# TYPES:

# home_airport: Airport object
# start_airport: key 
# end_airport: key 
# graph = dictionary, containing lists of Airport objects
# big_cost = float (this is the accumulated cost of travelling down an edge)
# visited_airports = list, containing strings that correspond to the keys on the graph

# '''

def createLowestPrice(home_airport, start_index, end_index, graph, big_cost, memo_dict, visited_airports):
    starter = list(graph)[start_index]
    print(list(graph))
    ender = list(graph[starter])[end_index]


    key_name = starter + ":" + ender
    if key_name in memo_dict:
        return memo_dict[key_name]

    visited = False

    if ender == home_airport:
        for key in graph:
            if key not in visited_airports:
                break
            else:
                visited = True

    if visited: 
        return visited_airports, big_cost #that's our fucking route
    elif start_index < 0 or end_index <0:
        return big_cost
    else:
        
        '''
        we either ARE adding the route, or we're NOT adding the route

        '''
        with_visit = list(map(lambda x: x, visited_airports))
        with_visit.append(starter)
        without_visit = visited_airports
        added = 0
        if starter == ender:
            added = 0
        else: 
            added = Route.calculate_score(graph[starter][starter], graph[starter][ender])

        memo_dict[key_name] = added
        q = big_cost + added

        our_min = min(min(createLowestPrice(home_airport,  start_index -1, end_index, graph, q,memo_dict, with_visit), createLowestPrice(home_airport, start_index -1, end_index, graph, big_cost, memo_dict, visited_airports)), min(createLowestPrice(home_airport,  start_index, end_index -1, graph, q,memo_dict, with_visit), createLowestPrice(home_airport, start_index, end_index-1, graph, big_cost, memo_dict, visited_airports)))
        return our_min

master()
