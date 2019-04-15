from Route import Route
from Aircraft import Aircraft




class Vertex: 
    def __init__(self, n, airport):
        self.name = n
        self.airport = airport

'''
    This version supports both weighted and unweighted edges. 
'''

class Graph:
    vertices = {}
    # we have this dictionary so that we can locate any vertex using its name
    edges = {}
    # our edge indices allow us to quickly locate any vertex indices via its name

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            # first check that what you're adding is indeed a vertex and that it's not in the vertices dictionary
            self.vertices[vertex.name] = vertex
            

    def add_edge(self, u, v, plane):
        edge_key = u.name + ":" + v.name

        if edge_key not in self.edges:
            if Route.calculate_distance(u.airport, v.airport) <= plane.getRange():
                self.edges[edge_key] = Route.calculate_score(u.airport, v.airport)

    def print_vertices(self):
        print(self.vertices)

    def print_edges(self):
        print(self.edges)

