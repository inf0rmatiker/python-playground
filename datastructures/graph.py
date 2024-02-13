from pprint import pprint, pformat
from . import stack, queue

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

    def get_weight(self, id: str) -> int:
        return self.neighbors[id]

    def add_neighbor(self, id: str, weight: int = 0):
        self.neighbors[id] = weight


# Graph is an undirected graph structure (bidirectional)
# with optionally weighted edges.
class Graph:
    def __init__(self, vertices = None):
        # Mappings of ids to Vertex objects
        self.vertices = vertices if vertices else {}
        self.vertex_count = len(self.vertices)

    def __str__(self):
        return pformat(self.vertices)

    def print(self):
        for vertex in self.vertices.keys():
            print(self.vertices[vertex])

    def add_edge(self, from_id: str, to_id: str, weight: int = 0):
        from_vertex: Vertex = self.vertices[from_id]
        from_vertex.add_neighbor(to_id, weight)

        to_vertex: Vertex = self.vertices[to_id]
        to_vertex.add_neighbor(from_id, weight)

    def add_vertex(self, id: str):
        self.vertices[id] = Vertex(id)

    def get_vertices(self):
        return self.vertices.keys()

    # Returns Vertex by id
    def get_vertex(self, id):
        if id in self.vertices:
            return self.vertices[id]
        return None

# --- Graph traversal algorithms ---

# Does a depth first traversal of a graph g
def depth_first_iterative(g: Graph, start: str):
    start_vertex: Vertex = g.get_vertex(start)
    if start_vertex is None:
        return

    visited = set()  # set of already-visited vertices
    visit_stack = stack.Stack()
    visit_stack.push(start_vertex)
    while visit_stack.size() > 0:

        # Pop the next vertex off the visit stack; visit it
        current: Vertex = visit_stack.pop()
        if current.get_id() not in visited:
            print(current)
            visited.add(current.get_id())

            # Add all its unvisited neighbors the visit stack
            for neighbor in current.get_neighbors():
                if neighbor not in visited:
                    visit_stack.push(g.get_vertex(neighbor))

def depth_first_recursive(g: Graph, current: str, visited: set):
    if current in visited or len(visited) == len(g.get_vertices()):
        return
    current_vertex: Vertex = g.get_vertex(current)
    print(current_vertex)
    visited.add(current)
    for neighbor in current_vertex.get_neighbors():
        if neighbor not in visited:
            depth_first_recursive(g, neighbor, visited)

def breadth_first_iterative(g: Graph, start: str):
    visited = set()
    to_visit = queue.Queue()
    to_visit.offer(start)

    while to_visit.size() > 0:
        current, _ = to_visit.poll()
        if current not in visited:
            current_vertex: Vertex = g.get_vertex(current)
            print(current_vertex)
            visited.add(current)
            # Add all the unvisited neighbors to the queue
            for neighbor in current_vertex.get_neighbors():
                if neighbor not in visited:
                    to_visit.offer(neighbor)

def shortest_path(g: Graph, start: str):
    infinity = 2**63 - 1
    visited = []
    unvisited = g.get_vertices()

    # Shortest distances from start
    distances = {}

    # How we got to this from start
    prev_vert = {}

    for vertex in g.get_vertices():
        if vertex == start:
            distances[vertex] = 0
        else:
            distances[vertex] = infinity

        # Still need to finish

    return