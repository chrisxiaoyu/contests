import c
import unittest


class TestContest712(unittest.TestCase):

    def test_problem_c(self):
        self.assertEqual(c.solve(6, 3), 4)
        self.assertEqual(c.solve(8, 5), 3)
        self.assertEqual(c.solve(22, 4), 6)


if __name__ == '__main__':
    unittest.main()
