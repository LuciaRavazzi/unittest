
from unittest.mock import Mock

# It's possible to configure the mock with
# - return_value 
mock = Mock(return_value = True)
print(mock())

# - side_effect 
mock = Mock(side_effect = print("3"))
print(mock())

# - name
mock = Mock(name = "My mock")
print(mock())