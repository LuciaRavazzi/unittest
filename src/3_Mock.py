

from unittest.mock import Mock

mock = Mock()
mock

# simulate the json library -> all functionalities are simulated; it can simulate any object.
json = mock

# The Mock() object create the method of that simulated function so that its interface can match the library's interface.
# the real dump() method of the json library is not present here.
json.dump()

# -> the simulated functions accept all the argument (in this way you can execute the code without errors). 
# It returns a Mock() in order to face complex situations!
# In this example, if the result isn't a Mock, how can the get function work?
json.loads('{"key": "value"}').get('key')

# You can understand the behavior of the function, like how many times it is called etc with assertion methods.
print(json.loads.call_count)
print(json.loads.call_args)
print(json.loads.call_args_list)
print(json.method_calls)


