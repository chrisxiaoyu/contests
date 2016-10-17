import c
import unittest


class TestContest540(unittest.TestCase):

    def test_problem_c(self):
        self.assertEqual(
            c.solve(
                4,
                6,
                [
                    'X...XX',
                    '...XX.',
                    '.X..X.',
                    '......'
                ],
                (1, 6),
                (2, 2)
            ),
            'YES'
        )
        self.assertEqual(
            c.solve(
                5,
                4,
                [
                    '.X..',
                    '...X',
                    'X.X.',
                    '....',
                    '.XX.'
                ],
                (5, 3),
                (1, 1)
            ),
            'NO'
        )
        self.assertEqual(
            c.solve(
                4,
                7,
                [
                    '..X.XX.',
                    '.XX..X.',
                    'X...X..',
                    'X......'
                ],
                (2, 2),
                (1, 6)
            ),
            'YES'
        )
        self.assertEqual(
            c.solve(
                2,
                2,
                [
                    '..',
                    'XX'
                ],
                (2, 1),
                (1, 1)
            ),
            'YES'
        )


if __name__ == '__main__':
    unittest.main()
