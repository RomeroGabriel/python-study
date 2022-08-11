# Conditionals

Material used to study: [W3Schools Conditionals](https://www.w3schools.com/python/python_conditions.asp)

## Logical conditional from mathematics

1. **Equals:** a == b
2. **Not Equals:** a != b
3. **Less than:** a < b
4. **Less than or equal to:** a <= b
5. **Greater than:** a > b
6. **Greater than or equal to:** a >= b

## Elif

```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```

## Short hand If

```python
if a > b: print("a is greater than b")
```

## Short Hand If ... Else

Known as **Ternary Operators** or **Conditional Expressions**

```python
print("A") if a > b else print("B")
```

### Multiple else statements

```python
print("A") if a > b else print("=") if a == b else print("B")
```
