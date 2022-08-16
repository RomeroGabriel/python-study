# Functions

Material used to study: [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

## Parameters

There is positional and keyword arguments. A general definition is:

```python
def function(pos1, pos2, /, pos_or_kwd, *, kwd1, kw2):
    # where pos = positional and
    # kwd = keyword
    pass
```

__IMPORTANT__: if `/` and `*` are not present if the functions definition, arguments may be passed to a function by position or by keyword.

### Positional-Only Paramenters

Positional-only parameters are placed before a `/`, that is used to logically separate the positional-only parameters from the rest of. If there is no `/` in the function, there are no positional-only parameters.

```python
def pos_only(arg, /):
    print(arg)
```

### Keyword-Only Parameters

Place a `*` before the arguments to indicate that the parameters must be keyword.

```python
def kwd_only_arg(*, arg):
    print(arg)
```

### Combined

```python
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```

### Arbitrary Positional Argument

```python
def multiples_arguments(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
```

## Higher Order Functions

A function that takes one or more functions as arguments or returns a function.
