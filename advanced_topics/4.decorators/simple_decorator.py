from typing import Callable

print('Start with DECORATORS!!!')

print('Add print (new behavior) to arithmetic functions')
def logged(func: Callable):
    print(f'    Adding loggin to {func.__name__}')

    def wrapper(*args, **kwargs):
        print(f'    You called {func.__name__}')
        return func(*args, **kwargs)

    return wrapper

@logged
def add(x, y):
    return x + y

@logged
def sub(x, y):
    return x - y

print(add(2, 3))
print(sub(2, 3))
print()
print('But when we print, function add or sub...')
print(add)
print(sub)
print('Both functions look like they are type like function logged')
print('To fix that, is necessary add some properties on logged function')

from functools import wraps

def logged_clean(func: Callable):
    print(f'    Adding loggin to {func.__name__} clean')

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'    You called {func.__name__} clean')
        return func(*args, **kwargs)
    return wrapper

@logged_clean
def add_clean(x, y):
    return x + y

@logged_clean
def sub_clean(x, y):
    return x - y

print()
print(add_clean(2, 3))
print(sub_clean(2, 3))
print(add_clean)
print(sub_clean)