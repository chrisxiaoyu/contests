import j
import unittest


class TestContest712(unittest.TestCase):

    def test_problem_c(self):
        self.assertEqual(
            j.solve(
                2,
                3,
                [
                    'U..',
                    '.*.'
                ]
            ),
            4
        )
        self.assertEqual(
            j.solve(
                4,
                4,
                [
                    'R...',
                    '.**.',
                    '.**.',
                    '....'
                ]
            ),
            12
        )
        self.assertEqual(
            j.solve(
                3,
                4,
                [
                    '***D',
                    '..*.',
                    '*...',
                ]
            ),
            6
        )


if __name__ == '__main__':
    unittest.main()
