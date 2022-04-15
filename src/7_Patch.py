import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch

# Usually, you use patch() as a decorator or a context manager to provide a scope in which you will mock the target object.
# Use patch() as a Decorator if you want to mock an object for the duration of your entire test function, you can use 
# patch() as a function decorator.

class TestCalendar(unittest.TestCase):
    @patch('my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()