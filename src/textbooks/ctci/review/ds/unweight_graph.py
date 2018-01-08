
class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            self.neighbors.sort()

class UnweightGraph(object):

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, from, to):
        if from in self.vertices and to in self.vertices:
            self.vertices[from.name].add_neighbor(to)
            self.vertices[to.name].add_neighbor(from)
            return True
        else:
            return False
