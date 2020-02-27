from hw4 import get_commit
import unittest
class Test_get_commit(unittest.TestCase):
    def test_print_commits(self):
        expect = {'Mocks': 10, 'Project1': 2, 'hellogitworld': 30, 'helloworld': 6, 'threads-of-life': 1}
        self.assertEqual(expect, get_commit("richkempinski"))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
