print('Starting with SORTING!!!')

numbers = [5, 2, 3, 1, 4]
print(f'Using as example list numbers {numbers}')
print(f'Sorting using sorted method:  {sorted(numbers)}')
print(f'    Do not change original array: {numbers}')

{numbers.sort()}
print(f'Sorting using list.sort() method:  return nothing')
print(f'    Change original array: {numbers}')

dict = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(f'Using sorted method to sort a dic (iterable). dic is {dict}')
print(f'Dic sorted: {sorted(dict)}')
print('    Just return the dict keys')


print()
print()

print('Starting using Key Functions')
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10)]
print(f'Using student tuples as exemple: {student_tuples}')
print(f'Sort by age (index 2): {sorted(student_tuples, key=lambda student: student[2])}')
print('Using python doc example with objects')
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(f'Student objects: {student_objects}')
print(f'Sort by age key: {sorted(student_objects, key=lambda student: student.age)}')


print('Starting with Operator Module Functions')
print('Using itemgetter() function operator to get item property on student_tuples')
from operator import itemgetter, attrgetter
print(f'    {sorted(student_tuples, key=itemgetter(2))}   sorted using key=itemgetter(2) -> by age')
print(f'    {sorted(student_tuples, key=itemgetter(2))}   sorted using key=itemgetter(2) -> by grade and age')

try:
    sorted(student_tuples, key=itemgetter(6))
except:
    print(f'    Except is throw when passed a number bigger than index (index out of range)')


print('Using attrgetter() function operator to get item property on student_objects')
print(f'    {sorted(student_objects, key=attrgetter("age"))}   sorted using key=attrgetter("age")')
print(f'    {sorted(student_objects, key=attrgetter("grade", "age"))}   sorted using key=attrgetter("grade", "age")')

try:
    sorted(student_objects, key=attrgetter("grade", "age", "corinthians"))
except:
    print(f'    Except is throw when passed attribute not present in object (object has no attribute "corinthians")')