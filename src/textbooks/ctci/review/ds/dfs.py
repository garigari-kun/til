
class Vertex(object):

    def __init__(self, name):
        self._name = name
        self.neighbors = []

        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    @property
    def name(self):
        return self._name

    def add_neighbor(self, neighbor):
        if not in self.neighbors:
            self.neighbors.append(neighbor)
            self.neighbors.sort()


class UnweightedGraph(object):

    def __init__(self):
        vertices = {}
        time = 0

    def add_vertex(self, vert):
        if isinstance(vert, Vertex) and vert.name not in self.vertices:
            self.vertices[vert.name] = vert
            return True
        else:
            return False

    def add_edge(self, v1, v2):
        if v1.name in vertices and v2.name in vertices:
            v1.add_neighbor(v2)
            v2.add_neighbor(v1)
            return True
        else:
            return False


    def _dfs(self, vert):
        vert.color = 'red'
        for neighbor in vert.neighbors:
            if neighbor.color == 'black':
                self._dfs(neighbor)


    def dfs(self, vert):
        self._dfs(vert)
