# Context Manager

Python documentation for more details: https://docs.python.org/3/reference/datamodel.html#context-managers

## With statement context manager

1. Handles the entry into, and exit from resources;
2. Normally invoked using the with statement but can be used by directly invoking their methods;
3. Typical uses of context managers: saving and restoring various kinds of global state, locking and unlocking resources, closing opened files, etc.

Methods:

1. object.__enter__(self)
    * Enter the runtime context releated to this object.
2. object.__exit__(self, exc_type, exc_value, traceback)
    * Exit the object runtime context;
    * The parameters describe the exeception that caused the context to be exited;
    * Without exeception, all three params will be None
    * If an exception is suppplied and wanna prevent it being propagated, it sould return a true value;