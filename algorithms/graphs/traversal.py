from datastructures.graph import Graph, Vertex, Edge, Cost
from datastructures.stack import Stack
from datastructures.queue import Queue
from datastructures.minheap import MinHeap

# Performs a DFS on a Graph g. Takes a current node starting point, and
# a set marking which nodes have already been visited.
def dfs(g: Graph, start):
    print("\nDepth-First Search:")
    visited = set()

    def dfs_helper(current):

        # If we've already visited this node, or we've visited all nodes,
        # just return.
        if current in visited or len(visited) == len(g.get_vertices()):
            return

        current_vertex: Vertex = g.get_vertex(current)
        print(current)
        visited.add(current)
        for neighbor in current_vertex.get_neighbors():
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)

# Performs a BFS on a Graph g, starting at the node specified by start.
def bfs(g: Graph, start):
    print("\nBreadth-First Search:")
    visited = set()
    to_visit = Queue()
    to_visit.offer(start)

    while to_visit.size() > 0:
        current, _ = to_visit.poll()
        if current not in visited:
            current_vertex: Vertex = g.get_vertex(current)
            print(current)
            visited.add(current)
            # Add all the unvisited neighbors to the queue
            for neighbor in current_vertex.get_neighbors():
                if neighbor not in visited:
                    to_visit.offer(neighbor)

# Dijkstra's Shortest Path algorithm, using a Priority Queue for the costs.
def shortest_paths(g: Graph, start):
    infinity = 2**63 - 1
    visited = set()

    # Distances from starting vertex
    distances = {}

    # How we got to each vertex from starting vertex
    prev_vert = {}

    # Set up distances set
    for vertex in g.get_vertices():
        if vertex == start:
            distances[vertex] = 0
        else:
            distances[vertex] = infinity

    # Set up priority queue
    costs = MinHeap()
    costs.push(Cost(weight=0, value=start))

    # Loop until we've visited every vertex
    while len(costs) > 0:
        # Start by visiting an unvisited vertex with the smallest known
        # distance from the start vertex. Pop a Cost off the MinHeap.
        cost, ok = costs.pop()
        current, current_distance = cost.value, cost.weight

        # Examine the current vertex's neighbors
        current_vertex: Vertex = g.get_vertex(current)
        for neighbor in current_vertex.get_neighbors():
            if neighbor not in visited:
                # Calculate the distance of each neighbor from the current vertex
                distance_to_neighbor_from_current = \
                    current_vertex.get_weight(neighbor) + current_distance

                # If the calculated distance is less than the currently known distance
                # to that vertex, update the distance to that neighbor and the prev
                # vertex with the current vertex. I.e, "We know that the shortest
                # way to get to this neighbor is through the current vertex".
                if distance_to_neighbor_from_current < distances[neighbor]:
                    distances[neighbor] = distance_to_neighbor_from_current
                    prev_vert[neighbor] = current

                    # Push this neighbor onto the queue of nodes to visit.
                    costs.push(
                        Cost(
                            weight=distance_to_neighbor_from_current,
                            value=neighbor
                        )
                    )

        # Mark the current vertex as visited, then remove it from unvisited
        visited.add(current)

    return distances, prev_vert

def print_shortest_paths(start, distances, prev_vert):
    print("\nDijkstra's Shortest Path:")
    print(f"Starting at vertex '{start}'")
    for key, val in distances.items():
        if key is not start:
            path = [key]
            curr = prev_vert[key]
            while curr is not start:
                path.insert(0, curr)
                curr = prev_vert[curr]
            path.insert(0, start)
            print(f"'{start}' to '{key}': distance={val}, path=[{' -> '.join(path)}]")


# Detects cycles in a directed graph. Does not work for undirected graphs.
def has_cycle(g: Graph) -> bool:
    print("\nCycle Detection:")
    visited = set()
    for node in g.get_vertices():
        # Only consider this node if it's not been visited already
        if node not in visited:

            # Create a set of all the nodes we see in this DFS call,
            # then perform a DFS to see if there's any cycles detected from
            # this node.
            visited_in_dfs_path = set()
            if cycle_dfs(g, node, visited, visited_in_dfs_path):
                print("Cycle detected in graph.")
                return True
    print("No cycles detected in graph.")
    return False

# Returns True if a cycle is detected, False otherwise.
def cycle_dfs(g, node, global_visited: set, dfs_visited: set) -> bool:
    print(f"At node {node}, dfs_visited={dfs_visited}")
    if node in dfs_visited:
        return True

    dfs_visited.add(node)
    vertex = g.get_vertex(node)
    for neighbor in vertex.get_neighbors():
        if cycle_dfs(g, neighbor, global_visited, dfs_visited):
            return True

    global_visited.add(node)
    dfs_visited.remove(node)
    return False
