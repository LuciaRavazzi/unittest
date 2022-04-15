
import unittest

from my_sum import sum

# Steps:
# - Import the function that you want to test.
# - Define some test through the unittest.TestCase.
# - For each test, define the input, the output that the function should return 
# - Add an assertion to compare the expected and the current output.

# In order to run the test, run:
# - python -m unittest -v test
# - python -m unittest discover
# - python -m unittest discover -s tests -> se dovessero esserci più test da fare.


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
