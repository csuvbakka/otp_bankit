import unittest
from matrix import traverse


class TestMatrixTraversal(unittest.TestCase):

    def test_3_by_3_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], traverse(matrix))

    def test_4_by_3_matrix(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
        self.assertEqual([1, 2, 3, 4, 8, 2, 1, 0, 9, 5, 6, 7], traverse(matrix))


if __name__ == '__main__':
    unittest.main()