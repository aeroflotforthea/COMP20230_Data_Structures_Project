
from Airport import Airport
from Route import Route
from Aircraft import Aircraft


plane = Aircraft("737", 5600, "LHR", "imperial")

madrid = Airport("Madrid", 3.7038, 40.4168, 0.84)
london = Airport("London", 0.1278, 51.5074, 1.17)
moscow = Airport("Moscow", 37.618423, 55.7558, 0.5)
shanghai = Airport("Shanghai", 121.4737, 31.2304, 0.4) 
paris = Airport("Paris", 2.3522 , 48.864716, 1.1)
hk = Airport("Hong Kong", 114.149139, 22.286394, 1)

# stops = {
#     "Madrid": [london, dublin, madrid],
#     "Dublin": [london, madrid, dublin],
#     "London": [madrid, dublin, london]
# }


'''
Step 1: 
Produce a dictionary with possibilities. 

'''




#

def build_dict_as_lists(list_of_airports, possibilities_lookup, plane):
    for i in range(len(list_of_airports)):
        possibilities_lookup[list_of_airports[i].getName()] = []
        for j in range(len(list_of_airports)):
            if i != j and Route.calculate_distance(list_of_airports[i], list_of_airports[j]) <= plane.getRange():
                possibilities_lookup[list_of_airports[i].getName()].append(list_of_airports[j])

    return possibilities_lookup

def build_dict_as_dictionaries(list_of_airports, possibilities_lookup, plane):
    for i in range(len(list_of_airports)):
        possibilities_lookup[list_of_airports[i].getName()] = {}
        for j in range(len(list_of_airports)):
            if i != j and Route.calculate_distance(list_of_airports[i], list_of_airports[j]) <= plane.getRange():
                possibilities_lookup[list_of_airports[i].getName()][list_of_airports[j].getName()] = list_of_airports[j]

    return possibilities_lookup


list_of_airports = [madrid, moscow, london, shanghai, hk]

possibilities = build_dict_as_dictionaries(list_of_airports, {}, plane)


'''

Here we present the flight options as a list
{   
    'Madrid': [<Airport.Airport object at 0x10788ddd8>, <Airport.Airport object at 0x10788dda0>], 
    'Moscow': [<Airport.Airport object at 0x10788d2b0>, <Airport.Airport object at 0x10788dda0>, <Airport.Airport object at 0x10788de10>], 
    'London': [<Airport.Airport object at 0x10788d2b0>, <Airport.Airport object at 0x10788ddd8>], 
    'Shanghai': [<Airport.Airport object at 0x10788ddd8>]
}

alternative: We present the flight options as a dictionary

{   
    'Madrid': { 
        "London": <Airport.Airport object at 0x10788ddd8>, 
        "Moscow": <Airport.Airport object at 0x10788dda0>
    }, 
    'Moscow': {
        "London": <Airport.Airport object at 0x10788d2b0>,
        "Moscow": <Airport.Airport object at 0x10788dda0>, 
        "Shanghai": <Airport.Airport object at 0x10788de10>
    }, 
    'London': {
        "Moscow": <Airport.Airport object at 0x10788d2b0>, 
        "Madrid": <Airport.Airport object at 0x10788ddd8>
    },
    'Shanghai': {
        "Moscow": <Airport.Airport object at 0x10788ddd8>
    }
}

'''


'''
costs = {
    "madrid": 
}
'''
# Now create a list of scores: 


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
now we have this: buildRouteCosts dictionary
{
    'Madrid': {
        'Madrid:Moscow': 2514.5086754189656, 
        'Madrid:London': 1060.5510120422184
    }, 
    'Moscow': {
        'Moscow:Madrid': 1496.731354416051, 
        'Moscow:London': 1241.4990162237787, 
        'Moscow:Shanghai': 3406.255512378663
    }, 
    'London': {
        'London:Madrid': 1477.1960524873757, 
        'London:Moscow': 2905.107697963642
    }, 
    'Shanghai': {
        'Shanghai:Moscow': 2725.0044099029305
    }
}

What we want to do next is: 
- If London was our start airport:
    - (London to Moscow or London to Madrid) * (Moscow to all destinations) * (Madrid to all destinations) * Shanghai to all destinations

How do we do that? 

1) Choose your route node e.g 'London'
2) For n keys in your root node ('London:Madrid', 'London:Moscow')
    create n possible routes, starting with the second half of the key


def createRoute(key, cost, description):
    for dict_key in buildRouteCosts[key]:
        destination = dict_key[len(key):]
        print(destination)

'''


def createRoute(key, cost, description, routes, home, complete_routes):
    for complete_route in complete_routes:
        if complete_route == description:
            return
    full_description = True
    for item in routes:
        if item not in description:
            full_description = False
            break
    
    if full_description and key == home:
        print("FULL ROUTE: ", description, cost)
    else:
        counter = 0
        for dict_key in routes[key]:
            destination = dict_key[len(key)+1:]
            if full_description and destination == home:
                    new_description = description
                    new_description += ":" + destination
                    new_cost = cost
                    new_cost += route_dictionary[key][dict_key]
                    if new_description not in complete_routes:
                        complete_routes.append({new_description: new_cost})
                    return
                
            if destination in description:
                counter += 1
                # this bit needs to change. We need to go through the routes and find the one that is closest to the home
                
                if counter == len(routes[key]):
                    for item in routes[key]:
                        if destination != home:
                            destination = dict_key[len(key)+1:]
                            new_description = description
                            new_description += ":" + destination
                            new_cost = cost
                            new_cost += route_dictionary[key][dict_key]
                            createRoute(destination, new_cost, new_description, routes, home, complete_routes)
                else:
                    continue
            else:
                new_description = description
                new_description += ":" + destination
                new_cost = cost
                new_cost += route_dictionary[key][dict_key]
                createRoute(destination, new_cost, new_description, routes, home, complete_routes)
    print(complete_routes)

createRoute('London', 0, "London", route_dictionary, "London", [])

'''

London: 
- do london:madrid 
     london:madrid:moscow
        london:madrid:moscow:shanghai
            london:madrid:moscow:shanghai:moscow
                london:madrid:moscow:shanghai:moscow:london
     london:moscow
        london:moscow:madrid
            london:moscow:madrid:london
    
for node in dictionary: 
    - add to the overall score
    - move us on 
    - don't try and go back if we've not visited everywhere
    - if we're home, add to routes.

on each iteration, we need to know: 
 - where home is
 - the overall score at that time
 - the stack of routes
 - 



London -> Madrid -> Moscow -> Shanghai -> Moscow -> London
London -> Moscow -> Madrid -> London 

Essentially: If you can return to the root node, do, and finish. 
'''

# manifest = {
#     "root": london,
#     "cost": 0,
#     "visited": [],
#     "list_of_airports": [london, moscow, madrid, shanghai],
#     "possibilities_lookup": possibilities,
#     "start_length": 3
# }

# def RF(n, manifest):

   

#     possibilities_key = manifest["list_of_airports"][n].getName()

#     manifest["visited"].append(possibilities_key)
#     # get an airport

#     airport_object = manifest["possibilities_lookup"][possibilities_key]
#     # airport_object is a dictionary containing nodes that the current airport can fly to


#     if manifest["start_length"] != n:
#         above_key  =  manifest["list_of_airports"][n+1].getName()
#         above_object = manifest["possibilities_lookup"][above_key]
#     # object of n
#     root_object = manifest["root"]


#     if n < 0:
#         return RF(n+1, manifest)
   
#     all_visited = True
#     for airport in manifest["list_of_airports"]:
#         if airport.getName() not in manifest["visited"]:
#             all_visited = False
#             break
    
#     if all_visited:
#         if manifest["root"] in manifest["possibilities_lookup"][possibilities_key].keys():
#             new_price = Route.calculate_score(manifest["list_of_airports"][n], root_object)
#             manifest["cost"] += new_price
#             manifest["visited"].append(manifest["root"].getName())
#             return manifest
#         else:
#             new_price = Route.calculate_score(airport_object, above_object)
#             manifest["visited"].append(above_key)
#             return RF(n+1, manifest)
#     else:
#         p1_key = manifest["list_of_airports"][n-1].getName() # Madrid
#         p2_key = manifest["list_of_airports"][n-2].getName()# Moscow

#         # loop through the possible destinations

#         if p1_key not in airport_object:
#             p1_score = float('inf')
#         else:
#             p1_score = Route.calculate_score(manifest["list_of_airports"][n], airport_object[p1_key])
#         if p2_key not in airport_object:
#             p2_score = float('inf')
#         else:
#             p2_score = Route.calculate_score(manifest["list_of_airports"][n], airport_object[p2_key])

#         if p1_score < p2_score:
#             manifest["cost"] += p1_score
#             # manifest["visited"].append(manifest["list_of_airports"][n-1])
#             return RF(n-1, manifest)
#         else: 
#             manifest["cost"] += p2_score
#             # manifest["visited"].append(manifest["list_of_airports"][n-2].getName())
#             return RF(n-2, manifest)

# print(RF(len(manifest["list_of_airports"]) -1, manifest))   

    
