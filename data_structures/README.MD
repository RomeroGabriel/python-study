# Data Structures

## Tuples
Can be initialized like t = 'AA', '2011-06-07', 100, 32.2 or t = ('AA', '2011-06-07', 100, 32.2)

..* Support unpacking
....+ name, date, shares, price = t
..* Immutable
....+ can't t[2] = 50
..* May be nested (creating a new tuple, of course since is immutable)
....+ u = t, (1, 2, 3, 4, 5)
..* But can contain mutable objects
....+ So the tuple can't change, however tuple's elements can
