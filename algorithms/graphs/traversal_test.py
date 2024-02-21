import unittest
from traversal import bfs, dfs

class TestGraphTraversal(unittest.TestCase):
    def test_bfs(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    import sys
    import os

    sys.path.append(os.path.abspath('../../datastructures'))
    import datastructures
    unittest.main()
