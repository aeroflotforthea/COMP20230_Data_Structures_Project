import math

import pandas as pd

class Airport:
    
    def __init__(self, name, airport_name, city_name, latitude, longitude, toEuro):
        self.__name = name
        self.__airport_name = airport_name
        self.__city_name = city_name
        self.longitude = longitude
        self.latitude = latitude
        self.__toEuro = toEuro
        
        '''
        RAPH EDIT - I've switched latitude and longitude round to conform to the airports dictionary
        
        '''
        
    def getAirportName(self):
        return self.__airport_name
    
    def getCityName(self):
        return self.__city_name
        
    def getExchangeRate(self):
        return self.__toEuro
    
    def getName(self):
        return self.__name
    
#     we don't use it
#     def setExchangeRate(self, new_exchange_rate):
#         self.__exchange_rate = new_exchange_rate
#         print("Exchange rate set to ", new_exchange_rate)
#         return self.getExchangeRate()



class Aircraft:
    def __init__(self, code, flight_range, units):
        self.code = code
        self.units = units
        self.flight_range = self.convertToMetric(flight_range)
        
        '''
        RAPH EDIT!!!! 
        
        I've removed home_aiport from the Aircraft object - we don't need it
        
        '''
    def convertToMetric(self, flight_range):
        if self.units == "imperial":
            return round(flight_range * 1.60934, 2)
        else:
            return flight_range
        
    def getRange(self):
        return self.flight_range
    
    def getName(self):
        return self.code



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


df_aircraft = pd.read_csv("aircraft.csv")

# turn all aircrafts into dictionary - key is aircraft code
aircraft_dict = df_aircraft.set_index('code').T.to_dict('list')


# WORKS


# # 
aircraftList =[]
for key in aircraft_dict.keys():
    aircraftList.append(key)


# WORKS



aircraftObjects = {} # this is the thislist
for aircraft in aircraftList:
    myobject = Aircraft((aircraft_dict[aircraft])[0], (aircraft_dict[aircraft])[4], (aircraft_dict[aircraft])[2])
    aircraftObjects[aircraft]=myobject
    
    


# WORKS
# '''
# RAPH EDIT - the aircraft object looks like this: Aircraft(code, flight range, units)
# '''


df_airportcurr = pd.read_csv("airportcurrency.csv")


airportcurr_dict = df_airportcurr.set_index('airportcode').T.to_dict('list')


airportList = []
for key in airportcurr_dict.keys():
    airportList.append(key)
    
airportObjects = {}
for airport in airportList:
    myobject = Airport((airportcurr_dict[airport])[0], (airportcurr_dict[airport])[1], (airportcurr_dict[airport])[2], (airportcurr_dict[airport])[4], (airportcurr_dict[airport])[5], (airportcurr_dict[airport])[7])
    airportObjects[airport]=myobject
    

# '''
# RAPH EDIT - The aiport object looks like this:
# Airport(name, airportname, cityname, longitude, latitude, toEuro)
# '''





list_of_airports = ['LHR', 'JFK', 'SVO', 'SXF','XDB']
list_of_airport_dict = {}

# list_airports_just = [airportObjects[x] for x in list_of_airports]
example_airports_list = [airportObjects[x] for x in list_of_airports]

# '''
# RAPH EDIT!!

# I'm renaming 'list_airports_just' to 'example_airports_list'
# '''

for i in list_of_airports:
    list_of_airport_dict[i] = airportObjects[i]



def build_flight_possibilities(list_of_airports, possibilities_lookup, plane):
    for i in range(len(list_of_airports)):
        possibilities_lookup[list_of_airports[i].getName()] = {}
        for j in range(len(list_of_airports)):
            if i != j and Route.calculate_distance(list_of_airports[i], list_of_airports[j]) <= plane.getRange():
                possibilities_lookup[list_of_airports[i].getName()][list_of_airports[j].getName()] = list_of_airports[j]

    return possibilities_lookup

# possibilities = build_flight_possibilities(example_airports_list, {}, aircraftObjects['747'])

def buildRouteCosts(list_of_airports, potential_routes):
    
    '''
    RAPH EDIT!!!
    
    I'm making buildRouteCosts take possibilities (potential_routes) as a parameter
    '''
    costs = {}

    for airport in list_of_airports: 
        costs[airport.getName()] = {}
        get_costs_from = potential_routes[airport.getName()]
        for key in get_costs_from: 
            costs_key = airport.getName() + ":" + key
            costs[airport.getName()][costs_key] = Route.calculate_score(airport, potential_routes[airport.getName()][key])

    return costs

# routes = buildRouteCosts(example_airports_list, possibilities)

def build_route_string(list_of_airports, string_route_lookup, plane):
    for i in range(len(list_of_airports)):
        string_route_lookup[list_of_airports[i].getName()] = []
        for j in range(len(list_of_airports)):
            if i != j and Route.calculate_distance(list_of_airports[i], list_of_airports[j]) <= plane.getRange():
                if list_of_airports[i].getName() in string_route_lookup:
                    string_route_lookup[list_of_airports[i].getName()].append(list_of_airports[j].getName())
                else:
                    string_route_lookup[list_of_airports[i].getName()]=list_of_airports[j].getName()

    return string_route_lookup

# mygraph=build_route_string(example_airports_list, {}, aircraftObjects['747'])

# home = "LHR"
def firstcost(home, graph, start, flightlist, routes, path =[],a=0, cost=0): 
    path = path + [start]
    cost+=a
    if len(path)==len(flightlist) and home in graph[start]:
        path.append(home)
        start_string = start +":" + home
        a = routes[start][start_string]
        cost += a
        return path, cost
    for node in graph[start]: 
        if node not in path: 
            start_string = start +":" + node
            a = routes[start][start_string]
            newpath = firstcost(home, graph, node, flightlist, routes,path,a, cost) 
            if newpath:  
                return newpath 
    return path, "Error: Aircraft is too small to successfully traverse flightplan"

# firstroute, boundcost = firstcost(mygraph, home, list_of_airports, routes)


def myDFS(home, graph, start, cost, flightlist, routes, boundcost, paths, path=[],a=0): 
    path=path+[start] 
#     print("path is", path)
    cost+=a
    if len(path)==len(flightlist) and home in graph[start]:
#         print("last cost is", cost)
        path.append(home)
        start_string = start +":" + home
        a = routes[start][start_string]
        cost += a        
        paths[cost]=path
    for node in graph[start]:
        start_string = start +":" + node
        a = routes[start][start_string]
        if node not in path and cost+a<boundcost:
#             print("node is", node)
            myDFS(home, graph,node,cost,flightlist,routes,boundcost,paths, path, a)
    return paths

# special_paths = myDFS(mygraph, home,0, list_of_airports, routes, boundcost, {})




def partitioner(items_to_sort, first_item, last_item):
    
    pivot = items_to_sort[first_item]
    left_point = first_item + 1
    right_point = last_item

    done = False
    while not done:

        while left_point <= right_point and items_to_sort[left_point] <= pivot:
            # if the item on the left is smaller than the pivot, move the left_point across (i.e ignore it)
               left_point = left_point + 1

                    
        while items_to_sort[right_point] >= pivot and right_point >= left_point:
               right_point = right_point -1
            # likewise, if the point on the right is bigger than the pivot, just close the right in towards the middle

        if right_point < left_point:
               done = True
        else:
            # switch them round
            temp_store = items_to_sort[left_point]
            items_to_sort[left_point] = items_to_sort[right_point]
            items_to_sort[right_point] = temp_store

    temp_store = items_to_sort[first_item]
    items_to_sort[first_item] = items_to_sort[right_point]
    items_to_sort[right_point] = temp_store


    return right_point
        
        
def actual_quick_sort(items_to_sort, first_item, last_item):
        if first_item < last_item:
            # this is our base case - once the first_item is the same as the last_item the recursion will stop.
            
            divider = partitioner(items_to_sort, first_item, last_item)
            
            actual_quick_sort(items_to_sort,first_item,divider-1)
            actual_quick_sort(items_to_sort,divider+1,last_item)
            
            
def sortMe(items_to_sort):
    actual_quick_sort(items_to_sort, 0, len(items_to_sort)-1)
    return items_to_sort
    

# paths = special_paths
# path_list = [key for key in paths]


# best_route = sortMe(path_list)[0]
# print("The cheapest route to take is ", paths[best_route], " and it costs ", best_route)


def BuildRoute():
    home_query = input("Please enter the code of your designated 'home' airport: ")
    print("Home has been set as: ", home_query, " - ", airportObjects[home_query].getAirportName(), " in ", airportObjects[home_query].getCityName())
    list_of_airports_query = "" 
    list_of_airports = []
    print("Please enter the codes of every airport you would like to travel to, not including ", home_query, ". Please type 'done' when you have finished entering destinations.")
    while list_of_airports_query != "done":
        list_of_airports_query = input("Enter the code of an airport:")
        if list_of_airports_query == "done":
            break
        if list_of_airports_query not in airportcurr_dict:
            print("That airport wasn't found.")
        else:
            list_of_airports.append(list_of_airports_query)
            print("airport successfully added.")
            print(list_of_airports)
    
    list_of_airports.append(home_query)
    print("The list of destinations you have entered is: ", list_of_airports, "with ", home_query, " as the start point.")
    plane_code = input("Please enter the code of the aircraft you would like to use.")
    
    dictionary_of_airports = {}

    # list_airports_just = [airportObjects[x] for x in list_of_airports]
    list_of_airport_objects = [airportObjects[x] for x in list_of_airports]

    '''
    RAPH EDIT!!

    I'm renaming 'list_airports_just' to 'example_airports_list'
    '''

    for i in list_of_airports:
        dictionary_of_airports[i] = airportObjects[i]

#     print(dictionary_of_airports)
#     print(list_of_airport_objects)
    
    plane = aircraftObjects[plane_code]
#     print(plane.getName())
    
    possibilities = build_flight_possibilities(list_of_airport_objects, {}, plane)
    
#     print("The flight graph looks like: ", possibilities)
    for key in possibilities: 
        if len(possibilities[key]) == 0:
            print("This is an invalid route for this aircraft. The aircraft's maximum range is too small to travel to one of the chosen destinations")
            return
        
    routes = buildRouteCosts(list_of_airport_objects, possibilities)
    mygraph= build_route_string(list_of_airport_objects, {}, plane)
    print(mygraph)
    print(routes)
    firstroute, boundcost = firstcost(home_query, mygraph, home_query, list_of_airports, routes)
    print(firstroute, boundcost)
    
    paths = myDFS(home_query, mygraph, home_query, 0, list_of_airports, routes, boundcost, {})
    
    path_list = [key for key in paths]

    best_route = sortMe(path_list)[0]
    
    print("The cheapest route to take is ", paths[best_route], " and it costs ", best_route)
    
   
BuildRoute()

    
    