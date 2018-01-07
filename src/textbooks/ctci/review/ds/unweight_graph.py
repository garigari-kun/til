
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
