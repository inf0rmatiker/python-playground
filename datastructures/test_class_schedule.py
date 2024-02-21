import unittest
import class_schedule

class TestCycles(unittest.TestCase):
    def test_cycles(self):
        # Single A -> B, no cycles
        nodes = ['A', 'B']
        edges = [['A', 'B']]
        cycles = class_schedule.Cycles()
        self.assertFalse(cycles.has_cycle(nodes, edges),
                         f"Found a cycle in graph")

        # Cycle from D back to A:
        #  A -> B -> C -> D
        #  ^______________|
        nodes = ['A', 'B', 'C', 'D']
        edges = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']]
        self.assertTrue(cycles.has_cycle(nodes, edges),
                         f"Did not find a cycle in graph")

        # Disjoint vertices, no cycles
        nodes = ['A', 'B', 'C']
        edges = []
        self.assertFalse(cycles.has_cycle(nodes, edges),
                        f"Found a cycle in graph")

        # More complex graph, cycle between D, F, E
        nodes = ['A', 'B', 'C', 'D', 'E', 'F']
        edges = [['A', 'B'], ['B', 'C'], ['B', 'D'], ['C', 'E'], ['D', 'F'],
                 ['F', 'E'], ['E', 'D']]
        self.assertTrue(cycles.has_cycle(nodes, edges),
                        f"Did not find a cycle in graph")


if __name__ == '__main__':
    unittest.main()
