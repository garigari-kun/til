import unittest


class Vertex(object):

    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

    def __str__(self):
        return '{} neighbors: {}'.format(self.key,
            [x.key for x in self.neighbors]
        )

class Graph(object):

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.vertices[key]
        except KeyError:
            return None

    def get_vertices(self):
        return self.vertices.keys()

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))

        self.vertices[from_key].add_neighbor(self.vertices[to_key], weight)


    def __add_vertex_if_not_in_vertices(self, key):
        if key not in self.vertices:
            self.add_vertex(Vertex(key))





if __name__ == '__main__':
    graph = Graph()
    v1 = Vertex("A")
    v2 = Vertex("B")
    graph.add_vertex(v1)
    graph.add_vertex(v2)
    print(graph.get_vertex("A"))
    print(graph.get_vertices())
    graph.add_edge("A", "B")
    print(graph.get_vertex("A"))
