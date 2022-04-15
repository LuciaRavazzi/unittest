import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock


# side_effect defines how the function should work when the Mock() function is called. 

requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

if __name__ == '__main__':
    unittest.main()