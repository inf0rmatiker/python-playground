# There are a total of num_courses courses you have to take,
# labeled from 0 to num_courses - 1. You are given an array prerequisites
# where prerequisites[i] = [ai, bi] indicates that you must take course
# bi first if you want to take course ai.
from typing import List


# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def can_finish(self, num_courses: int, prerequisites) -> bool:

        # Create adjacency list
        adj = {i: [] for i in range(num_courses)}

        # Add dependencies
        for pre_list in prerequisites:
            prereq = pre_list[1]
            target = pre_list[0]
            adj[prereq].append(target)

        global_visited = set()
        for node in adj.keys():
            if node not in global_visited:
                dfs_visited = set()
                if not self.dfs(node, adj, global_visited, dfs_visited):
                    return False
        return True

    def dfs(self, node: int, adj, global_visited, dfs_visited) -> bool:
        # We've been here before
        if node in dfs_visited:
            return False

        dfs_visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in global_visited:
                if not self.dfs(neighbor, adj, global_visited, dfs_visited):
                    return False

        global_visited.add(node)
        return True

class Cycles:

    # Detects cycles in a directed graph
    def has_cycle(self, nodes: list, edges: list) -> bool:
        # Construct adjacency list
        adj = {node: [] for node in nodes}
        for edge in edges:
            adj[edge[0]].append(edge[1])

        visited = set()
        for node in nodes:
            if node not in visited:
                visited_in_dfs_path = set()
                if self.dfs(node, adj, visited, visited_in_dfs_path):
                    return True
        return False

    # Does a recursive Depth-First Search a graph starting from a node.
    # Returns True if a cycle is detected, False otherwise.
    def dfs(self, node, adj: dict, global_visited: set, dfs_visited: set) -> bool:

        # Base case, we've seen this node before in the DFS path
        if node in dfs_visited:
            return True

        dfs_visited.add(node)
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, global_visited, dfs_visited):
                return True

        # We didn't detect any cycles, so mark this node as globally visited
        global_visited.add(node)
        return False

class Solution2:
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> \
    List[int]:

        # Create adjacency list
        adj = {i: [] for i in range(num_courses)}

        # Add dependencies
        for pre_list in prerequisites:
            prereq = pre_list[1]
            target = pre_list[0]
            adj[prereq].append(target)

        print(adj)

        global_visited = set()
        order = [-1 for i in range(num_courses)]
        # Start at the end of order, we'll be filling it in reverse order
        index = num_courses - 1

        # Try every node in adj list, so we don't miss disjoint graphs
        for node in adj.keys():
            # Skip globally visited nodes
            if node not in global_visited:
                # dfs_visited tracks the nodes we've visited on our DFS traversal
                # This makes sure we catch a cycle if a node appears twice
                dfs_visited = set()

                # Update index with how far back this DFS traversal made it
                ok, index = self.dfs(node, adj, global_visited, dfs_visited,
                                     order, index)

                # Not ok means we found a cycle, so just return an empty list.
                # This graph cannot be topologically traversed
                if not ok:
                    return []
        return order

    # Returns a bool (can be finished), and the new index of where to insert
    # the next prerequisite node
    def dfs(self, node: int, adj, global_visited, dfs_visited, order, i) -> (
    bool, int):
        # We've been here before
        if i < 0 or node in dfs_visited:
            return False, -1

        dfs_visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in global_visited:
                ok, i = self.dfs(neighbor, adj, global_visited, dfs_visited,
                                 order, i)
                if not ok:
                    return False, -1

        # We've found all the nodes this node is a prerequisite for,
        # go ahead and add ourselves to the ordered list and move back a space
        order[i] = node
        global_visited.add(node)
        return True, i - 1