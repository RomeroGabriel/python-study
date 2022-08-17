# Closure

The way to use nested functions and return the nested function to be executed.

[For more information](https://www.programiz.com/python-programming/closure)

## Nonlocal variable in a nested function

1. A functions defined inside another functions is called a nested function;
2. Variables of the enclosing scope can be accessed by the nested function (non-local variables);
3. Non-local variables are read-only by default. To modify them, is necessary use `nonlocal` keyword (not good ideia i think).

## Features

1. To be closure, we need return the nested function
2. So in this way, we can postpone the function execution
3. We can allocate a variable to receive the function

## When use closure?

1. Avoid use of global values;
2. When is necessary provide some form of data hiding;
3. When one or few methos are implement in a class;
