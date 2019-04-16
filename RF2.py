
from Airport import Airport
from Route import Route
from Aircraft import Aircraft


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
# dublin = Airport("Dublin", )

print("plane range is ", plane.getRange())
print(Route.calculate_distance(hk, la))

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


list_of_airports = [paris, dublin, london, NYC, hk, hawaii, shanghai]

possibilities = build_dict_as_dictionaries(list_of_airports, {}, plane)

# print(possibilities)


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


def buildRouteCosts(list_of_airports, home):
    costs = {}

    for airport in list_of_airports: 
        costs[airport.getName()] = {}
        get_costs_from = possibilities[airport.getName()]
        for key in get_costs_from: 
            costs_key = airport.getName() + ":" + key
            costs[airport.getName()][costs_key] = (Route.calculate_score(airport, possibilities[airport.getName()][key]), Route.calculate_distance(airport, home))
    return costs


route_dictionary = buildRouteCosts(list_of_airports, dublin)
print(route_dictionary)

# print(route_dictionary)
# print(route_dictionary)
# print(route_dictionary)

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


def createRoute(key, came_from, cost, description, routes, home, complete_routes, banned_routes):
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
                    new_cost += routes[key][home_key][0]
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
                            new_cost += routes[key][item][0]
                            return createRoute(potential_destination, key, new_cost, new_description, routes, home, complete_routes, banned_routes)
            if counter == len(routes[key]):
                
                # this means we've tried to go everywhere, which means we have to go back to where we came from
                # but we need to put a check in place to prevent feedback loops

                # we need to try and return everywhere possible destination

                smallest = float('inf')
                for destination_key in routes[key]:
                    if routes[key][destination_key][1] < smallest:
                        potential_destination = destination_key[len(key)+1:]
                        special_key = destination_key
                new_description = description
                new_description += ":" + potential_destination
                new_cost = cost
                new_cost += routes[key][special_key][0]
                return createRoute(potential_destination, key, new_cost, new_description, routes, home, complete_routes, banned_routes)


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
            new_cost += routes[key][dict_key][0]
            createRoute(destination, key, new_cost, new_description, routes, home, complete_routes, banned_routes)
    return complete_routes

print(createRoute('Dublin', 'Dublin', 0, "Dublin", route_dictionary, "Dublin", {}, []))

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

{
    'London:Madrid:Moscow:Paris:Athens:London': 9912.807199356335, 
    'London:Madrid:Moscow:Athens:Paris:London': 7568.238211131004, 
    'London:Madrid:Paris:Moscow:Athens:London': 8492.837792306851, 
    'London:Madrid:Paris:Athens:Moscow:London': 8046.178216135153, 
    'London:Madrid:Athens:Moscow:Paris:London': 6778.5782871153815, 
    'London:Madrid:Athens:Paris:Moscow:London': 9008.970474993244, 
    'London:Moscow:Madrid:Paris:Athens:London': 9874.446409320342, 
    'London:Moscow:Madrid:Athens:Paris:London': 8326.42829204099, 
    'London:Moscow:Paris:Madrid:Athens:London': 9023.9363455198, 
    'London:Moscow:Paris:Athens:Madrid:London': 9253.549694866717, 
    'London:Moscow:Athens:Madrid:Paris:London': 6921.851784573183, 
    'London:Moscow:Athens:Paris:Madrid:London': 8214.514396642024, 
    'London:Paris:Madrid:Moscow:Athens:London': 7433.448363380874, 
    'London:Paris:Madrid:Athens:Moscow:London': 6363.370251105667, 
    'London:Paris:Moscow:Madrid:Athens:London': 8457.090762023885, 
    'London:Paris:Moscow:Athens:Madrid:London': 7039.643176624282, 
    'London:Paris:Athens:Madrid:Moscow:London': 8192.065473345983, 
    'London:Paris:Athens:Moscow:Madrid:London': 7481.427425233995, 
    'London:Athens:Madrid:Moscow:Paris:London': 8643.345779169214, 
    'London:Athens:Madrid:Paris:Moscow:London': 9287.527172085476, 
    'London:Athens:Moscow:Madrid:Paris:London': 7665.160620729441, 
    'London:Athens:Moscow:Paris:Madrid:London': 8349.797596276454, 
    'London:Athens:Paris:Madrid:Moscow:London': 9668.46128091027, 
    'London:Athens:Paris:Moscow:Madrid:London': 10163.09991893509
}

London, paris, moscow, madrid, hong kong:

{
    'London:Madrid:Moscow:Paris:Moscow:Hong Kong:Moscow:London': 19913.5776572201, 
    'London:Madrid:Moscow:Hong Kong:Moscow:Paris:London': 16306.392474375529, 
    'London:Madrid:Paris:Moscow:Hong Kong:Moscow:London': 16950.573867291787, 
    'London:Paris:Madrid:Moscow:Hong Kong:Moscow:London': 15891.184438365812, 
    'London:Paris:Moscow:Madrid:Moscow:Hong Kong:Moscow:London': 19081.279755991156
}

paris, london, athens, hong kong, shanghai, honolulu

{
    'Paris:London:Athens:Hong Kong:Honolulu:Shanghai:Athens:Paris': 38019.18263010905, 
    'Paris:London:Athens:Shanghai:Honolulu:Hong Kong:Athens:Paris': 38867.93531635087, 
    'Paris:Athens:London:Athens:Hong Kong:Honolulu:Shanghai:Athens:Paris': 42331.29275209203, 
    'Paris:Athens:London:Athens:Shanghai:Honolulu:Hong Kong:Athens:Paris': 43180.045438333844
}

{
    'Paris': {'Dublin': <Airport.Airport object at 0x10d588128>, 'London': <Airport.Airport object at 0x10d5855f8>, 'New York': <Airport.Airport object at 0x10d5880f0>}, 
    'Dublin': {'Paris': <Airport.Airport object at 0x10d585f98>, 'London': <Airport.Airport object at 0x10d5855f8>, 'New York': <Airport.Airport object at 0x10d5880f0>}, 
    'London': {'Paris': <Airport.Airport object at 0x10d585f98>, 'Dublin': <Airport.Airport object at 0x10d588128>, 'New York': <Airport.Airport object at 0x10d5880f0>}, 
    'New York': {'Paris': <Airport.Airport object at 0x10d585f98>, 'Dublin': <Airport.Airport object at 0x10d588128>, 'London': <Airport.Airport object at 0x10d5855f8>, 'Honolulu': <Airport.Airport object at 0x10d5880b8>},
    'Hong Kong': {'Honolulu': <Airport.Airport object at 0x10d5880b8>, 'Shanghai': <Airport.Airport object at 0x10d585f60>}, 
    'Honolulu': {'New York': <Airport.Airport object at 0x10d5880f0>, 'Hong Kong': <Airport.Airport object at 0x10d585fd0>, 'Shanghai': <Airport.Airport object at 0x10d585f60>}, 'Shanghai': {'Hong Kong': <Airport.Airport object at 0x10d585fd0>, 'Honolulu': <Airport.Airport object at 0x10d5880b8>}
    }

'''