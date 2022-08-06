from typing import Callable
from functools import wraps

print('Basically add one more function that receives the arguments')

def repeat(num_times: int):
    def decorator_repeat(func: Callable):
        @wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

print('Calling decorator to repeat 4 times the function')
@repeat(num_times=4)
def corinthians():
    print(f'VAMOS, VAMOS CORINTHIANS')

corinthians()