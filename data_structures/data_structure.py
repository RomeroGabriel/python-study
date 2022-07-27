from audioop import reverse


print('Starting with TUPLES!!!')
print()
t = 'AA', '2011-06-07', 100, 32.2
print(f"Tuple example is: t = {t}")
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
print(f"List example is: fruits = {fruits}")
print(f'fruits count: {fruits.count("apple")}')
print(f'banana index: {fruits.index("banana")}')
print(f'reverse fruits {fruits.reverse()} CHANGING THE ORIGINAL LIST {fruits}')
print('**')
print('To reverse a list without change original list, is necessary to copy (with other reference object) and reverse or use slice(better)')
print('Link for more information: https://stackoverflow.com/questions/41777333/how-to-reverse-a-list-without-modifying-the-original-list-in-python')
print('**')
fruits.append("grape")
print(f'add element grape: fruits is {fruits}')
fruits.insert(1, "pineapple")
print(f'add element pineapple on index 1: fruits is {fruits}')
print(f'sort fruits {fruits.sort()} CHANGING THE ORIGINAL LIST {fruits}')
print(f'remove last object from fruits using pop and retorn the element: {fruits.pop()}. Fruits now is: {fruits}')

print()
print()

print('Starting with SETS!!!')
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(f"Set example is: basket = {basket}")

print('Good for membership test')
print(f'orange is in basket? {"orange" in basket}')
print(f'Corinthians is in basket? {"Corinthians" in basket}')


a = set('abracadabra')
b = set('alacazam')
print(f'set a {a} and set b {b}')
print(f'check letters in a but not in b? a - b { a - b}')
print(f'check letters in a or  b or both? a | b { a | b}')
print(f'check letters both in a and b? a & b { a & b}')
print(f'check letters in a or b but not both? a ^ b { a ^ b}')