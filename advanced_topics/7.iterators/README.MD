# Iterators

Material used to study:

1. [W3Schools Iterator](https://www.w3schools.com/python/python_iterators.asp)
2. [Programiz Iterator](https://www.programiz.com/python-programming/iterator)
3. [Python: Functional Programming HOWTO iterators](https://docs.python.org/3/howto/functional.html#iterators)
4. [Python: Functional Programming HOWTO Creating new iterators](https://docs.python.org/3/howto/functional.html#creating-new-iterators)
5. [Python: Itertools](https://docs.python.org/3/library/itertools.html)

An iterator is an object that contains a countable number of values. This object can be iterated upon, traversing through all the values. To be a iterator object, the object needs implements the iterator protocal, which consist of the method `__iter__()` and `__next__()`.

When `__next__()` is call and there is no more elements to pass (so all elements from the iterator was passed), a `StopIteration` exception is raised.

Iterators don't need to be finite, it's perfectly reasonable write an iterator that produces an infinite stream of data.

## Iterator vs Iterable

An object is called __iterable__ if we can get a __iterator__ from it. List, tuple, dict, and set are all iterable object. They are iterable containers which you can get an iterator from.

The `iter()` built-in function (which in turn calls the `__iter__()` method) returns an iterator from them.

```python
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) # take the next item from iterator
print(next(myit))
print(next(myit))
```

## Functions creating iterators for efficient looping

[On this link](https://docs.python.org/3/library/itertools.html) there is a lot functions to create new iterators. Good for functional programming.

## Building Custom Iterators

```python
class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0 # create n
        return self

    def __next__(self):
        if self.n <= self.max: # check conditional else StopIteration
            result = 2 ** self.n
            self.n += 1 # look like recursion
            return result
        else:
            raise StopIteration


numbers = PowTwo(3)
i = iter(numbers)
print(next(i))
print(next(i))
```

```python
class InfIter:
    """Infinite iterator to return all odd numbers"""
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
```
