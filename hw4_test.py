from hw4 import get_commit
import unittest
class TestHW(unittest.TestCase):

    def test_print_commits(self):
        self.assertEqual(get_commit('richkempinski'),
                         "{'Mocks': 10, 'Project1': 2, 'hellogitworld': 30, 'helloworld': 6, 'threads-of-life': 1}")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
