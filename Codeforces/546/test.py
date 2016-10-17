import c
import unittest


class TestContest546(unittest.TestCase):

    def test_problem_c(self):
        self.assertEqual(c.solve(4, [2, 1, 3], [2, 4, 2]), '6 2')
        self.assertEqual(c.solve(3, [1, 2], [2, 1, 3]), -1)


if __name__ == '__main__':
    unittest.main()
