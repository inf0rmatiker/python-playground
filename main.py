from datastructures import graph, class_schedule, minheap
from datastructures.graph import Graph
from algorithms.graphs.traversal import dfs, bfs, \
    print_shortest_paths, shortest_paths, has_cycle

def graph_tests():
    print("* Graph Traversal Tests *")
    g = Graph(vertices=None, is_directed=True)

    for vertex in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        g.add_vertex(vertex)

    for edge in [
        ('A', 'B', 1),
        ('A', 'C', 5),
        ('B', 'E', 2),
        ('C', 'D', 1),
        ('D', 'E', 3),
        ('D', 'F', 1),
        ('D', 'G', 5),
        ('E', 'F', 2)
    ]:
        g.add_edge(edge[0], edge[1], weight=edge[2])

    dfs(g, start='A')
    bfs(g, start='A')

    distances, prev_vert = shortest_paths(g, start='A')
    print_shortest_paths('A', distances, prev_vert)

    has_cycle(g)


def main():
    graph_tests()


if __name__ == "__main__":
    main()
