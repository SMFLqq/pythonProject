import time

def time_function(function):

    def wrapper(*args, **kwargs):

        start_time = time.time()

    result = function(*args, **kwargs)

    end_time = time.time()

    print(f'Time taken to execute {function.__name__}: {end_time - start_time} seconds')
    return result
    return wrapper

    def some_function():
        time.sleep(1)
        return

    def test_time_function():
        some_function()

    test_time_function()