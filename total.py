# ================= IMPORTS =============== #
from Airport import Airport
from Route import Route
from Aircraft import Aircraft

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
print(route_dictionary)

'''

'''