import a
import unittest


class TestContest522(unittest.TestCase):

    def test_problem_a(self):
        self.assertEqual(
            a.solve(
                5,
                [
                    ['tourist', 'reposted', 'Polycarp'],
                    ['Petr', 'reposted', 'Tourist'],
                    ['WJMZBMR', 'reposted', 'Petr'],
                    ['sdya', 'reposted', 'wjmzbmr'],
                    ['vepifanov', 'reposted', 'sdya'],
                ]
            ),
            6
        )
        self.assertEqual(
            a.solve(
                6,
                [
                    ['Mike', 'reposted', 'Polycarp'],
                    ['Max', 'reposted', 'Polycarp'],
                    ['EveryOne', 'reposted', 'Polycarp'],
                    ['111', 'reposted', 'Polycarp'],
                    ['VkCup', 'reposted', 'Polycarp'],
                    ['Codeforces', 'reposted', 'Polycarp'],
                ]
            ),
            2
        )
        self.assertEqual(
            a.solve(
                1,
                [
                    ['SoMeStRaNgEgUe', 'reposted', 'PoLyCaRp']
                ]
            ),
            2
        )


if __name__ == '__main__':
    unittest.main()
