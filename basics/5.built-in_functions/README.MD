# Built-in Functions

Material used to study: [Built-in Functions](https://docs.python.org/3/library/functions.html)

Here will be just mention the most important ones (in my point of view). If necessary, some functions will be presented in code example.

## A

### abs(x)

Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing __abs__(). If the argument is a complex number, its magnitude is returned.

### all(iterable)

Return `True` if all elements of a iterable are true (or if the iterable is empty).

### any()

Return `True` if any element of the iterable is true. If the iterable is empty, return `False`.

## C

### callable(object)

Return `True` if the object argument appears callable, `False` if not. Note that, instances of a classes are callable if their class has a __call__() method.

### @classmethod

Transform a method into a class method. Is a function decorator. Is different than C++ AND Java static methods, for these behavior use `staticmethod()` on this section. Two aways to call the method:

```python
# Code example
class C:
    @classmethod
    def f(cls, arg1, arg2): ...

```

1. Called from a class: `C.f()`;
2. Called from a instance: `C().f()`.

If a class method is called for a derived class, the derived class object is passed as the implied first argument.

## D

### delatt(object, name)

Deletes the named attribute. The string must be the name of one of object's attributes. `delattr(x, 'foobar')` is equivalent to `del x.foobar`.

### dict(**kwarg), dict(mapping,**kwarg), dict(iterable,**kwarg)

Create a new dictionary. Examples to init a dict:

```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
a == b == c == d == e == f
True
```

### dir([object])

Without arguments, return the list of names in the current local scope. With argument, attempt to return a list of valid attributes for that object.

1. If the object is a module object: list contains the names of the module's attributes;
2. If the object is a class object: list contains the names of its attributes and recursively of the attributes of its bases;
3. Otherwise, everything.

```python
import struct
dir()   # show the names in the module namespace  
['__builtins__', '__name__', 'struct']

dir(struct)   # show the names in the struct module 
['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__initializing__', '__loader__', '__name__', '__package__',
 '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']

class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']
s = Shape()
dir(s)
['area', 'location', 'perimeter']
```

### divmod(a, b)

TO DO ...
