import b
import unittest


class TestContest389(unittest.TestCase):

    def test_problem_b(self):
        self.assertEqual(
            b.solve(
                5,
                [
                    ['.', '#', '.', '.', '.'],
                    ['#', '#', '#', '#', '.'],
                    ['.', '#', '#', '#', '#'],
                    ['.', '.', '.', '#', '.'],
                    ['.', '.', '.', '.', '.']
                ]
            ),
            'YES'
        )
        self.assertEqual(
            b.solve(
                3,
                [
                    ['.', '#', '.'],
                    ['#', '#', '#'],
                    ['.', '#', '#'],
                ]
            ),
            'NO'
        )
        self.assertEqual(
            b.solve(
                3,
                [
                    ['.', '#', '.'],
                    ['#', '#', '#'],
                    ['.', '#', '.'],
                ]
            ),
            'YES'
        )
        self.assertEqual(
            b.solve(
                6,
                [
                    ['.', '#', '.', '.', '#', '.'],
                    ['#', '#', '#', '#', '#', '#'],
                    ['.', '#', '#', '#', '#', '.'],
                    ['.', '#', '#', '#', '#', '.'],
                    ['#', '#', '#', '#', '#', '#'],
                    ['.', '#', '.', '.', '#', '.'],
                ]
            ),
            'NO'
        )
        self.assertEqual(
            b.solve(
                3,
                [
                    ['.', '.', '.'],
                    ['.', '.', '.'],
                    ['.', '.', '.'],
                ]
            ),
            'YES'
        )


if __name__ == '__main__':
    unittest.main()
