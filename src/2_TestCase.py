
# In order to organize better the test, unittest module help us.
# It requires to put the test inside the method of a class and inside each of them, an assertion
# statement is executed.

# In this way, it is easier to understand which is the test that is OK and the one that failed.

import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

    
        