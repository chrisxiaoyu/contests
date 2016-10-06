import c
import unittest


class TestContest510(unittest.TestCase):

    def test_problem_c(self):
        self.assertEqual(
            c.solve(
                10,
                [
                    [2, 1],
                    [3, 1],
                    [4, 2],
                    [5, 1],
                    [6, 2],
                    [7, 5],
                    [8, 6],
                    [9, 8],
                    [10, 5],
                ],
                [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 1, 1, 1, 0, 1]
            ),
            [4, 7]
        )
        self.assertEqual(
            c.solve(
                3,
                [
                    [1, 2],
                    [1, 3],
                ],
                [1, 1, 1],
                [0, 0, 0]
            ),
            [1, 2, 3]
        )


if __name__ == '__main__':
    unittest.main()
