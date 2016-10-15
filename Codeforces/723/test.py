import d
import unittest


class TestContest723(unittest.TestCase):

    def test_problem_d(self):
        self.assertEqual(
            d.solve(
                5,
                4,
                1,
                [
                    ['*', '*', '*', '*'],
                    ['*', '.', '.', '*'],
                    ['*', '*', '*', '*'],
                    ['*', '*', '.', '*'],
                    ['.', '.', '*', '*'],
                ]
            ),
            (
                1,
                [
                    ['*', '*', '*', '*'],
                    ['*', '.', '.', '*'],
                    ['*', '*', '*', '*'],
                    ['*', '*', '*', '*'],
                    ['.', '.', '*', '*'],
                ]
            )
        )
        self.assertEqual(
            d.solve(
                3,
                3,
                0,
                [
                    ['*', '*', '*'],
                    ['*', '.', '*'],
                    ['*', '*', '*']
                ]
            ),
            (
                1,
                [
                    ['*', '*', '*'],
                    ['*', '*', '*'],
                    ['*', '*', '*']
                ]
            )
        )
        self.assertEqual(
            d.solve(
                4,
                4,
                0,
                [
                    ['*', '*', '*', '*'],
                    ['*', '.', '.', '*'],
                    ['*', '.', '.', '*'],
                    ['*', '*', '*', '*']
                ]
            ),
            (
                4,
                [
                    ['*', '*', '*', '*'],
                    ['*', '*', '*', '*'],
                    ['*', '*', '*', '*'],
                    ['*', '*', '*', '*']
                ]
            )
        )


if __name__ == '__main__':
    unittest.main()
