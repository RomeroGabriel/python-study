from audioop import reverse


print('Starting with TUPLES!!!')
print()
t = 'AA', '2011-06-07', 100, 32.2
print(f"Tuple exaple is: t = {t}")
## Looks a little bit like an array
print(f'Length of tuple T is {len(t)}')
print(t[0])
 
 ## Supports unpacking
name, date, shares, price = t
print(name, date, shares, price)

try:
    t[2] = 50
except:
    print('Tuples are immutable man')

print(f"Even tuples are immutable, if the tuple's elements is mutable, they can change:")
v = ([1, 2, 3], [3, 2, 1])
print(f'V: {v}')
element = v[1]
element.extend([9, 8, 7])
print(f'V: {v} alter second elements add 9, 8 ,7')

print('Can be nested to other tuple')
u = t, (1, 2, 3, 4, 5)
print(f'Result of two tuple nested {u}')
print(f'Length of u: {len(u)}')

print()
print()

print('Starting with LISTS!!!')
print()
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(f"Tuple exaple is: fruits = {fruits}")
print(f'fruits count: {fruits.count("apple")}')
print(f'banana index: {fruits.index("banana")}')
print(f'reverse fruits {fruits.reverse()} CHANGING THE ORIGINAL LIST {fruits}')
print('**')
print('To reverse a list without change original list, is necessary to copy (with other reference object) and reverse or use slice(better)')
print('Link for more information: https://stackoverflow.com/questions/41777333/how-to-reverse-a-list-without-modifying-the-original-list-in-python')
print('**')
print(f'add element grape: {fruits.append("grape")} fruits is {fruits}')
print(f'sort fruits {fruits.sort()} CHANGING THE ORIGINAL LIST {fruits}')
print(f'remove last object from fruits using pop and retorn the element: {fruits.pop()}. Fruits now is: {fruits}')

print()
print()

print('Starting with SETS!!!')