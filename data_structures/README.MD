# Data Structures

Python documentation for more details: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

## Tuples
Can be initialized like fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

1. Support unpacking
    * name, date, shares, price = t
2. Immutable
    * can't t[2] = 50
3. May be nested (creating a new tuple, of course since is immutable)
    * u = t, (1, 2, 3, 4, 5)
4. But can contain mutable objects
    * So the tuple can't change, however tuple's elements can


## Lists
Can be initialized like names = ['Gabriel', 'IBM', 'Corinthians', 'CAT']

1. Mutable
2. Usually(not necessary) all elements are of the same type