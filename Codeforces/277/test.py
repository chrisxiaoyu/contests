import a
import unittest


class TestContest377(unittest.TestCase):

    def test_problem_a(self):
        self.assertEqual(
            a.solve(
                5,
                5,
                [
                    [1, 2],
                    [2, 2, 3],
                    [2, 3, 4],
                    [2, 4, 5],
                    [1, 5]
                ]
            ),
            0
        )
        self.assertEqual(
            a.solve(
                8,
                7,
                [
                    [0],
                    [3, 1, 2, 3],
                    [1, 1],
                    [2, 5, 4],
                    [2, 6, 7],
                    [1, 3],
                    [2, 7, 4],
                    [1, 1]
                ]
            ),
            2
        )
        self.assertEqual(
            a.solve(
                2,
                2,
                [
                    [1, 2],
                    [0]
                ]
            ),
            1
        )
        self.assertEqual(
            a.solve(
                3,
                3,
                [
                    [0],
                    [0],
                    [0]
                ]
            ),
            3
        )
        self.assertEqual(
            a.solve(
                5,
                5,
                [
                    [1, 3],
                    [0],
                    [0],
                    [2, 4, 1],
                    [0]
                ]
            ),
            4
        )


if __name__ == '__main__':
    unittest.main()
