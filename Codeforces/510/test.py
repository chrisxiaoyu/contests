import b
import c
import unittest


class TestContest510(unittest.TestCase):

    def test_problem_b(self):
        self.assertEqual(b.solve(2, 2, ['AA', 'AA']), 'Yes')
        self.assertEqual(b.solve(3, 4, ['AAAA', 'ABCA', 'AAAA']), 'Yes')
        self.assertEqual(b.solve(3, 4, ['AAAA', 'ABCA', 'AADA']), 'No')
        self.assertEqual(
            b.solve(4, 4, ['YYYR', 'BYBY', 'BBBY', 'BBBY']),
            'Yes'
        )
        self.assertEqual(
            b.solve(
                7,
                6,
                [
                    'AAAAAB',
                    'ABBBAB',
                    'ABAAAB',
                    'ABABBB',
                    'ABAAAB',
                    'ABBBAB',
                    'AAAAAB'
                ]
            ),
            'Yes'
        )
        self.assertEqual(
            b.solve(2, 13, ['ABCDEFGHIJKLM', 'NOPQRSTUVWXYZ']),
            'No'
        )

    def test_problem_c(self):
        self.assertEqual(
            c.solve(3, ['rivest', 'shamir', 'adleman']),
            'bcdefghijklmnopqrsatuvwxyz'
        )
        self.assertEqual(
            c.solve(
                10,
                [
                    'tourist',
                    'petr',
                    'wjmzbmr',
                    'yeputons',
                    'vepifanov',
                    'scottwu',
                    'oooooooooooooooo',
                    'subscriber',
                    'rowdark',
                    'tankengineer'
                ]
            ),
            'Impossible'
        )
        self.assertEqual(
            c.solve(
                10,
                [
                    'petr',
                    'egor',
                    'endagorion',
                    'feferivan',
                    'ilovetanyaromanova',
                    'kostka',
                    'dmitriyh',
                    'maratsnowbear',
                    'bredorjaguarturnik',
                    'cgyforever'
                ]
            ),
            'agnhjlopefikdmbcqrstuvwxyz'
        )


if __name__ == '__main__':
    unittest.main()
