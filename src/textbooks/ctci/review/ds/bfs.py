class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self._distance = 9999
        self._color = 'black'

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, distance):
        self._distance = distance

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            self.neighbors.sort()


class Graph(object):

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, f, t):
        if f.name in self.vertices and t.name in self.vertices:
            self.vertices[f.name].add_neighbor(t)
            self.vertices[t.name].add_neighbor(f)
            return True
        else:
            return False



def bfs(vertex):
    queue = []
    vertex.distance = 0
    vertex.color = 'red'
    for v in vertex.neighbors:
        v.distance = vertex.distance + 1
        queue.append(v)

    while len(queue) > 0:
        target_ver = queue.pop(0)
        target_ver.color = 'red'

        for v in target_ver.neighbors:
            if v.color == 'black':
                queue.append(v)
                v.distance = target_ver.distance + 1



if __name__ == '__main__':
    graph = Graph()
    v1 = Vertex("A")
    v2 = Vertex("B")
    graph.add_vertex(v1)
    graph.add_vertex(v2)
    graph.add_edge(v1, v2)
    bfs(v1)
