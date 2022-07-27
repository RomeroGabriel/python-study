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

## Sets

Can be initialized like basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} or using set('alacazam')
Operations remembers the Set theory from math.

1. Eliminate all duplicates
2. Unordered

## Dictionaries

Can be initialized like tel = {'jack': 4098, 'sape': 4139} or dict(sape=4139, guido=4127, jack=4098)

1. Key-Value
2. Indexed by keys
3. Keys can be any immutable type: strigs, numbers or tuples (if the tuple only contains strings, numbers and tuples).
4. Keys are unique
5. If you store using a key that is already in use, the old value associated with that key is forgotten.