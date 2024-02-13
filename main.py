from datastructures import graph

def main():

    g = graph.Graph()

    for vertex in ['A', 'B', 'C', 'D', 'E']:
        g.add_vertex(vertex)

    for edge in [
        ('A', 'B', 5),
        ('A', 'C', 1),
        ('B', 'C', 3),
        ('B', 'E', 2),
        ('C', 'D', 4),
        ('D', 'E', 7),
    ]:
        g.add_edge(edge[0], edge[1], weight=edge[2])

    g.print()

    print("---- Depth First Iterative ----")
    graph.depth_first_iterative(g, 'A')

    print("---- Depth First Recursive ----")
    graph.depth_first_recursive(g, 'A', set())

    print("---- Breadth First Iterative ----")
    graph.breadth_first_iterative(g, 'A')


if __name__ == "__main__":
    main()
