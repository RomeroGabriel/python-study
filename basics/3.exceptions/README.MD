# Exceptions

Material used to study:

1. [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
2. [Python Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
3. [Real Python Exceptions](https://realpython.com/python-exceptions/)

All exceptions must be instances of a class that derives from `BaseException`.

## Handiling Exceptions

### Selected Exceptions

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```

### Multiple handlers expcetions

```python
try:
    x = int(input("Please enter a number: "))
    break
except (ValueError, TypeError, NameError):
    print("Oops!  That was no valid number.  Try again...")
```

### BaseExceptions as a wildcard

Since all exceptions inherit from `BaseException` is possible to use an to grab all exceptions.

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

### Try...except Else clause

Is possible to use Else clause in try...except statement. Is optional. Is useful for code that must be executed if the try clause does not raise an exception.

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

### Getting the exception

The except clause may specify a variable after the exception name. So, is possible to see more information about the exception

```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))   # <class 'Exception'>
    print(inst.args)    # ('spam', 'eggs')
    print(inst)         # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
                        #('spam', 'eggs')
    x, y = inst.args    # unpack args
    print('x =', x)     # x = spam
    print('y =', y)     # y = eggs
y = eggs
```

## Raising Exceptions

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

### Raise exception but don't handle it

```python
try:
    raise NameError('Hi There')
except NameError:
    print('An exception flew by!')
    raise
```

## Exceptions Chaining

The `raise` statement allows an options `from` which enables chaining exceptions.

```python
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

## User-definied Exceptions

Exceptions class should be derived directly or indirectly by the `Exception` class. Most exceptions are defined with names that end in `Error`.

## Exceptions Context

An exception may be handled when an `except` or `finally` or `with` statement is used. When raising a new exception while another exceptions is already being handled, the new exception's __context__ att is automatically set to the handled exception. This implicit exceptions context can be supplemented with an exception cause using `from`

```python
raise new_exc from original_exc
```

After `from` mus be an exception or None.

```python
raise new_exc from None
```

When is none, replaces the old exception with the new one for display purposes. The old exception is available in __context__ for instrospection when debugging.

## List of Exceptions

[Exception hierarchy link](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
