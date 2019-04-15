'''

 - you take in a list of airports
 - the cost of airport n to all the other airports is calculated (for loop)


 def calc(airport, list_of_airports):
     for key in list_of_airports:



'''

from Airport import Airport
from Route import Route
from Aircraft import Aircraft


plane = Aircraft("737", 5600, "LHR", "imperial")

madrid = Airport("Madrid", 3.7038, 40.4168, 0.84)
london = Airport("London", 0.1278, 51.5074, 1.17)
moscow = Airport("Moscow", 37.618423, 55.7558, 0.5)
shanghai = Airport("Shanghai", 121.4737, 31.2304, 0.4) 

# stops = {
#     "Madrid": [london, dublin, madrid],
#     "Dublin": [london, madrid, dublin],
#     "London": [madrid, dublin, london]
# }


'''
Step 1: 
Produce a dictionary with possibilities. 

'''



list_of_airports = [madrid, moscow, london, shanghai]
#

def build_dict(list_of_airports, possibilities_lookup, plane):
    for i in range(len(list_of_airports)):
        possibilities_lookup[list_of_airports[i].getName()] = []
        for j in range(len(list_of_airports)):
            if i != j and Route.calculate_distance(list_of_airports[i], list_of_airports[j]) <= plane.getRange():
                possibilities_lookup[list_of_airports[i].getName()].append(list_of_airports[j])

    return possibilities_lookup

# lookup_table = build_dict(list_of_airports, {}, plane)







'''

signature is a string that tracks where you've been 


def fuckit(the node that you're on right now, signature):

    The node that you're on could be an index
    if the index is < than 0 you've really tried to go everywhere you can go, 
    so you just return the signature

    [london, moscow, beijing, shanghai]

    if the index is less than 0, we have nowhere else we can go
        so just return

    signature += start_node_name


    if you're back home and you've been everywhere:
        return signature because you're done and it will definitely be the smallest

    otherwise you want to return the minimum of 


    # this means that you need to register where you are on each call, and the signature has all of the airports in it

    if you haven't been everywhere, create a subset n/including where you've been, and set off down those routes
    either with a node or without a node 


    return min(fuckit(n-1, signature), fuckit(n-2, signature))


    else: 
        calculate the minimum of all previous calls on left and all previous calls on right

    return 
    // going down different paths


'''

'''

def please(home, n, signature):

    if n < 0:
        return

    signature += list_of_airports[n].getName()

    for name in airport_names:
        if name not in signature or list_of_airports[n].getName() != home:
            continue
        else:
            return signature

    return get_score(list_of_airports[n], list_of_airports[n-1])
    
    

'''

airport_thing = {
    "list_of_airports": [london, moscow, madrid, shanghai],
    "signature": "",
    "home_airport": london,
    "airport_names": ["London", "Moscow", "Madrid", "Shanghai"],
    "score": 0,
    "plane": plane
}

def please(n, airport_thing):

    if n < 0 or n > len(airport_thing["list_of_airports"]):
        return 0 

    # if you're trying to access a bad index just return

    if Route.calculate_distance(airport_thing["list_of_airports"][n-1], airport_thing["list_of_airports"][n-2]) > airport_thing["plane"].getRange():
        return 0
    # likewise, if you're trying to go somewhere you can't just return 


    airport_thing["signature"] += list_of_airports[n].getName() + ":" + list_of_airports[n+1].getName()

    # but otherwise, update the airport thing signature
    
    for name in airport_names:
        if name not in signature or list_of_airports[n].getName() != home:
            continue
        else:
            return airport_thing
    
    original_airport_thing = dict(airport_thing)

    # we need to keep a copy of the airport thing because in one of the calls we're going to update it, and in another we're not going to

    airport_thing["score"] += Route.calculate_score(airport_thing[list_of_airports[n]], airport_thing[list_of_airports[n+1]])

    return min(please(n-1, original_airport_thing), please(n-1, airport_thing))
    
    
please(len(airport_thing["list_of_airports"]), airport_thing)