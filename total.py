# ================= IMPORTS =============== #
from Airport import Airport
from Route import Route
from Aircraft import Aircraft
import math

# ================= IMPORTS =============== #

'''

CLASSES! 

Airport, Aircraft and Route

'''


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

'''
Placeholder plane and airports:
'''

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



'''
First cost calculates the cost of the first possible route
'''

def firstcost(graph, start, flightlist, path =[],a=0, cost=0): 
    path = path + [start]
    cost+=a
    if len(path)==len(flightlist) and home in graph[start]:
        path.append(home)
        cost += getcost(start, home, costgraph)
        return path, cost
    for node in graph[start]: 
        if node not in path: 
            a = getcost(start, node, costgraph)
            newpath = firstcost(graph, node, flightlist, path,a, cost) 
            if newpath:  
                return newpath 
    return None


'''
myDFS generates all possible routes, and cuts if they're more expensive than first cost

'''

def myDFS(graph,start,cost,flightlist, bestcost, path=[],a=0): 
    path=path+[start] 
#     print("path is", path)
    cost+=a
    if len(path)==len(flightlist) and home in graph[start]:
#         print("last cost is", cost)
        path.append(home)
        cost += getcost(start, home, costgraph)
        paths[cost]=path
    for node in childrenOf(start):
        a = getcost(start, node, costgraph)
        if node not in path and cost+a<bestcost:
#             print("node is", node)
            myDFS(graph,node,cost,flightlist, bestcost,path,a)


'''

build_dict_as_dictionaries creates a graph, where each node contains the airports it can travel to

'''

def build_dict_as_dictionaries(list_of_airports, possibilities_lookup, plane):
    for i in range(len(list_of_airports)):
        possibilities_lookup[list_of_airports[i].getName()] = {}
        for j in range(len(list_of_airports)):
            if i != j and Route.calculate_distance(list_of_airports[i], list_of_airports[j]) <= plane.getRange():
                possibilities_lookup[list_of_airports[i].getName()][list_of_airports[j].getName()] = list_of_airports[j]

    return possibilities_lookup


'''
dummy list of airports
'''
list_of_airports = [paris, dublin, london, NYC, hk, hawaii, shanghai]

'''
possibilities is an example graph
'''

possibilities = build_dict_as_dictionaries(list_of_airports, {}, plane)

# print(possibilities)
'''

buildRouteCosts actually creates a dictionary with all possible destinations and equivalent scores for anywhere that it can go.

'''


def buildRouteCosts(list_of_airports):
    costs = {}

    for airport in list_of_airports: 
        costs[airport.getName()] = {}
        get_costs_from = possibilities[airport.getName()]
        for key in get_costs_from: 
            costs_key = airport.getName() + ":" + key
            costs[airport.getName()][costs_key] = Route.calculate_score(airport, possibilities[airport.getName()][key])

    return costs

route_dictionary = buildRouteCosts(list_of_airports)
# print(route_dictionary)

'''
{
    'Paris': 
        {
            'Paris:Dublin': 780.0759054937671, 'Paris:London': 333.5502847177977, 'Paris:New York': 5826.998279614931
        }, 
    'Dublin': 
        {
            'Dublin:Paris': 780.0759054937671, 'Dublin:London': 478.94735797307936, 'Dublin:New York': 5105.20687270428
        }, 
    'London': 
        {
            'London:Paris': 390.2538331198233, 'London:Dublin': 560.3684088285028, 'London:New York': 6525.510531597366
        }, 
    'New York': 
        {
            'New York:Paris': 8740.497419422396, 'New York:Dublin': 7657.81030905642, 'New York:London': 8366.039143073547, 'New York:Honolulu': 11981.72070267967
        }, 
    'Hong Kong': 
        {
            'Hong Kong:Honolulu': 2676.311457346746, 'Hong Kong:Shanghai': 369.11887089279065
        }, 
    'Honolulu': 
        {
            'Honolulu:New York': 11981.72070267967, 'Honolulu:Hong Kong': 13381.557286733729, 'Honolulu:Shanghai': 11908.038132162477
        }, 
    'Shanghai': 
        {
            'Shanghai:Hong Kong': 492.1584945237209, 'Shanghai:Honolulu': 3175.4768352433275
        }
}


'''


'''

RAPH'S CREATE ROUTE ALGORITHM


'''


def createRoute(key, came_from, cost, description, routes, home, complete_routes):
    for complete_route in complete_routes:
        if complete_route == description:
            return
    full_description = True
    for item in routes:
        if item not in description:
            full_description = False
            break
    
    counter = 0
    for dict_key in routes[key]:
        destination = dict_key[len(key)+1:]
        if destination in description:
            # this bit needs to change. We need to go through the routes and find the one that is closest to the home
            counter += 1
                
            if full_description: 
                # if we reach this point, it means that we've been everywhere 
                # firstly, check if we can go home:
                home_key = key + ":" + home
                if home_key in routes[key]:
                    new_description = description
                    new_description += ":" + home
                    new_cost = cost
                    new_cost += routes[key][home_key]
                    if new_description not in complete_routes:
                        complete_routes[new_description] = new_cost
                    return
                else:
                    for item in routes[key]:
                        potential_destination = item[len(key)+1:]
                        home_key = potential_destination + ":" + home
                        if home_key in routes[potential_destination]:
                            new_description = description
                            new_description += ":" + potential_destination
                            new_cost = cost
                            new_cost += routes[key][item]
                            return createRoute(potential_destination, key, new_cost, new_description, routes, home, complete_routes)
            if counter == len(routes[key]):
                
                # this means we've tried to go everywhere, which means we have to go back to where we came from
                # but we need to put a check in place to prevent feedback loops

                # we need to try and return everywhere possible destination
                smallest = [float('inf'), "", ""]
                for destination_key in routes[key]:
                    potential_destination = destination_key[len(key)+1:]
                    location = description.index(potential_destination)
                    if location <= smallest[0]:
                        smallest = [location, destination_key, potential_destination]

                new_description = description
                new_description += ":" + smallest[2]
                new_cost = cost
                new_cost += routes[key][smallest[1]]
                return createRoute(smallest[2], key, new_cost, new_description, routes, home, complete_routes)


                # back_key = key + ":" + came_from
                # banned_key = came_from + ":" + key
                # if back_key in banned_routes:
                #     continue
                # else:
                #     banned_routes.append(banned_key)
                # new_description = description
                # new_description += ":" + came_from
                # new_cost = cost
                # new_cost += routes[key][back_key]
                # return createRoute(came_from, key, new_cost, new_description, routes, home, complete_routes, banned_routes)
            else: 
                continue
        else:
            new_description = description
            new_description += ":" + destination
            new_cost = cost
            new_cost += routes[key][dict_key]
            createRoute(destination, key, new_cost, new_description, routes, home, complete_routes)
    return complete_routes

print(createRoute('Dublin', 'Dublin', 0, "Dublin", route_dictionary, "Dublin", {}))