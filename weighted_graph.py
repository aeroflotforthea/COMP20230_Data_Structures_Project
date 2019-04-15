from Airport import Airport
from Aircraft import Aircraft
from Route import Route
from adjacency_matrix import Vertex, Graph


def salesman(home_vertex, start_vertex, previous_vertex, subset, price_table, current_price, visited):
    name_key = ""
    if len(subset) == 0:
        name_key = start_vertex + ":" + home_vertex
        # return the price of the start_vertex to the home_vertex
        return price_table[home_vertex]
    else:
        name_key = start_vertex + ":" + previous_vertex
        current_price += price_table[name_key]
        visited.append(name_key)
        return min(salesman(home_vertex, subset[0], start_vertex, [x for x in subset if x != subset[0]], price_table, current_price, visited), salesman(home_vertex, subset[0], start_vertex, [x for x in subset if x != subset[1]], price_table, current_price, visited))
        


plane = Aircraft("737", 5600, "LHR", "imperial")
madrid = Airport("Madrid", 3.7038, 40.4168, 0.84)
london = Airport("London", 0.1278, 51.5074, 1.17)
dublin = Airport("Dublin", 6.2603, 53.3498, 1)
berlin = Airport("Berlin", 13.4050, 13.4050, 1.99) 

print(madrid.getName())

our_graph = Graph()

plane = Aircraft("737", 5600, "LHR", "imperial")
airport_list = [madrid, london, dublin, berlin]

for airport in airport_list:
    x = Vertex(airport.getName(), airport)
    our_graph.add_vertex(x)

for i in range(len(our_graph.vertices)):
    for j in range(len(our_graph.vertices)):
        if i != j:
            our_graph.add_edge(our_graph.vertices[list(our_graph.vertices)[i]], our_graph.vertices[list(our_graph.vertices)[j]], plane)
   

subset = [x.getName() for x in airport_list]

salesman("Dublin", "Dublin", subset[0], subset, our_graph.edges, 0, [])
