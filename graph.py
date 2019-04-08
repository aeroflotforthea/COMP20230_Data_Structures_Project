


def buildGraph(list_of_airport_objects, airplane_object):
    # first thing: build the graph object
    my_graph = {}

    for airport in list_of_airport_objects:
        my_graph[airport] = []
    
    for airport in list_of_airport_objects:
        for i in range(len(list_of_airport_objects)):
            if list_of_airport_objects[i] != airport:
                if Route.calculate_distance(list_of_airport_objects[i], airport) <= airplane_object.getRange():
                    my_graph[list_of_airport_objects[i].getName()].append(airport)
                    
    return my_graph


