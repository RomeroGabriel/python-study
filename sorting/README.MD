# Sorting

Python documentation for more details: https://docs.python.org/3/howto/sorting.html

There's two built-in fuctions for the job.
1. list.sort() method that modifies the list in-place (mutable and only works with lists)
2. sorted() method that builds a new sorted list from an interable (immutable and works on any iterable)

Sorts are stable, meaning that when multiple records have the same key, their original order is preserved.

## Sorting Basics

1. Default sorted ascending

## Key Functions

1. both sorted() and list.sort() have a key parameter.
2. Use to specify a function to be called on each element
3. Works for objects

## Operator Module Functions

1. The Python's module 'operator' provides convenience functions to make accessor functions easier and faster.
2. Allow multiple levels of sorting

## Ascending and Descending

1. Just use 'reverse' parameter with boolean True