from pprint import pprint, pformat

# Vertex is a structure mapping an id to a set of neighbors and the weight
# it costs to reach them.
class Vertex:

    def __init__(self, id: str):
        self.id = id

        # Mapping of neighbors to weights, i.e:
        # { 'b' -> 5, 'g' -> 7 }
        self.neighbors = {}

    def __str__(self):
        return f"Vertex {{id: '{self.id}', neighbors: {self.neighbors}}}"

    def get_id(self) -> str:
        return self.id

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_weight(self, name: str) -> int:
        return self.neighbors[name]

    def add_neighbor(self, name: str, weight: int = 0):
        self.neighbors[name] = weight


class Edge:

    def __init__(self, from_id, to_id, weight = 0):
        self.from_id = from_id
        self.to_id = to_id
        self.weight = weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __str__(self):
        return f"{{from_id={self.from_id}, to_id={self.to_id}, weight={self.weight}}}"

    def __repr__(self):
        return self.__str__()


# Graph is an undirected graph structure (bidirectional)
# with optionally weighted edges.
class Graph:
    def __init__(self, vertices = None, is_directed = False):
        # Mappings of ids to Vertex objects
        self.vertices = vertices if vertices else {}
        self.is_directed = is_directed

    def __str__(self):
        return pformat(self.vertices)

    def print(self):
        for vertex in self.vertices.keys():
            print(self.vertices[vertex])

    def add_edge(self, from_id: str, to_id: str, weight: int = 0):
        from_vertex: Vertex = self.vertices[from_id]
        from_vertex.add_neighbor(to_id, weight)

        if not self.is_directed:
            to_vertex: Vertex = self.vertices[to_id]
            to_vertex.add_neighbor(from_id, weight)

    def add_vertex(self, name: str):
        self.vertices[name] = Vertex(name)

    def get_vertices(self):
        return self.vertices.keys()

    # Returns Vertex by id
    def get_vertex(self, name):
        if name in self.vertices:
            return self.vertices[name]
        return None

class Cost:

    def __init__(self, weight: int, value):
        self.weight = weight
        self.value = value

    def __le__(self, other):
        return self.weight <= other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __str__(self):
        return f"{{weight={self.weight}, value={self.value}}}"

    def __repr__(self):
        return self.__str__()
