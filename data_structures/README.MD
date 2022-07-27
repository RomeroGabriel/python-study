# Data Structures

## Tuples
Can be initialized like t = 'AA', '2011-06-07', 100, 32.2 or t = ('AA', '2011-06-07', 100, 32.2)

1. Support unpacking
    * name, date, shares, price = t
2. Immutable
    * can't t[2] = 50
3. May be nested (creating a new tuple, of course since is immutable)
    * u = t, (1, 2, 3, 4, 5)
4. But can contain mutable objects
    * So the tuple can't change, however tuple's elements can