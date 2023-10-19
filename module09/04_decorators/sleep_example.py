from time import time, sleep
    
def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took', time() - t)
    return wrapper

@measure
def sleepy_function(sleep_time):
    sleep(sleep_time)

sleepy_function(0.3)
sleepy_function(0.5)