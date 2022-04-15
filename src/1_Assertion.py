
# In this script, some unit test case are performed. However, 
# these are simple tests and if something fails, maybe it is not so easy to
# understand at which point. So, test runners come in. 

if __name__ == "__main__":

    # 1. Unit test -> you're testing only one component (sum).
    assert sum([2, 2, 2]) == 6, "Should be 6"

    assert sum([1, 2, 2]) == 6, "Should be 6"
