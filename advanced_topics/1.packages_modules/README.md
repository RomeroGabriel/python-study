# Packages and Modules

Material used to study:

1. [Python Modules doc](https://docs.python.org/3/tutorial/modules.html)
2. [Python: Modules and Packages](https://www.youtube.com/watch?v=UK97NoQK23k)
3. [Real Python Modules and Packages](https://realpython.com/python-modules-packages/)

## Modules

A module is a file containing Python definitions and statements. The file name is the module name (without the .py extension). Within a module, the module's name (as a string) is available as the value of the global variable `__name__`.

The imported module names, if placed at the top level of a module (outside any function or classe), are added to the module's global namespace.

A file called `__init__.py` define a folder as a module. There are three different ways to define a module in Python:

1. A module written in Python;
2. A module written in C and loaded dynamically at run-time;
3. A built-in module.

### Import modules

**namespace is a list of methods and classes available to the current program.

```python
# fibo.py
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

```python
# Import module name to current namespace
import fibo # fibo is the module name (also the file name)

fibo.fib(10)
fibo.fib2(10)
```

```python
# Imports names(fib, fib2) from fib module into the importing module's namespace
from fibo import fib, fib2
# fibo is not defined
fib(10)
fib2(10)
```

```python
# Import all names from the module, except those beginning with an underscore(_)
from fibo import *
fib(10)
```

### Absolute imports

Is an absolute `import` where you fully specify the location of the classes being imported.

```python
# import PACKAGE(Drawing).MODULE(point-call)
import Drawing.point-call
P1 = point-call.Point()

# from PACKAGE(Drawing).MODULE(point-call) import CLASS
from Drawing.point-call import Point
P1 = Point()

# from PACKAGE(Drawing) import MODULE(point-call)
from Drawing import point-call
P1 = point-call.Point()
```

### Relative imports

Relative imports specific the location of the classes to be imported relative to the current package.

1. Current directory(package): `.`
2. Previous directory(package): `..`

```python
from .Point-docstrings import Point # If the files is in the same place.

from ..Point-docstrings import Point # If the file calling Pointdocstrings is one diretory down
```

### Fill `__init__.py`

```python
# in __init__.py
from .Point-docstrings import Point
```

Now is possible say:

```python
import Drawing.Point
```

Instead of:

```python
# Is kind converts the Drawing package into a module
import Drawing.Point-docstrings.Point
from Drawing import Point
```

### Executing modules as scripts (`__main__`)

Any python file that contains a module is also a Python __script__ and can be executed when is imported.

```python
if __name__ == "__main__"
    # start script
```

The code above will prevent the module to be executed when is imported. This make the file usable as script as well as an importable module.

## Packages

Is a set of modules. Allow a hierarchical structuring of the module namespace using __dot notation__. In the same way that `modules` help avoid collisions between global variables names, `packages` help avoid collisions between module names.

### Imports

Take this folder structure as example.
![Folder structure example](https://github.com/RomeroGabriel/python-study/blob/main/advanced_topics/1.packages_modules/folder_structure_example.png "Folder structure example")

1. Import individual module form the packages:

```python
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

2. Alternative away of import submodule:

```python
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)
```

3. Import the desired function or class or variable

```python
# loads the submodule echo, but this makes its function echofilter() directly available
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)
```

`from package import item`, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable.

`import item.subitem.subsubitem`, each item except for the last must be a package. The last item can be a module or a package but can't be a class or function or variable defined in the previous item.

### Importing * from a Package and using `__all__`

Importing everything can take a long time and have unwanted side-effects. It's not recommend. Defining a list named `__all__` in `__init__.py` file can define which modules should be imported when `from package import *` is encountered.

```python
# in sound/effects__init__.py
__all__= ["echo", "surround", "reverse"]
# will import just this 3 modules
```

### Intra-package references

```python
from . import echo
from .. import formats
from ..filters import equalizer
```