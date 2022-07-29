print('Starting with GROUPBY ITERTOOLS!!!')

from itertools import groupby

print('Using as example: AAAABBBCCD')
print('Grouping without key:')
group = groupby("AAAABBBCCDAABBB")
for key, value in group:
    print(f'    {key}, {list(value)}')

data = [
    {
        'name': 'AA',
        'price': '32.2',
        'share': '100',
    },
    {
        'name': 'CAT',
        'price': '83.44',
        'share': '150',
    },
    {
        'name': 'GE',
        'price': '40.37',
        'share': '95',
    },
    {
        'name': 'IBM',
        'price': '91.1',
        'share': '50',
    },
    {
        'name': 'IBM',
        'price': '70.44',
        'share': '100',
    },
    {
        'name': 'MSFT',
        'price': '65.1',
        'share': '50',
    },
    {
        'name': 'MSFT',
        'price': '51.23',
        'share': '200',
    },
]

print()
print()

print(f'Using as example: {data} already sorted')
print('Grouping without data by name:')

data_name = groupby(data, key= lambda e: e['name'])
for key, value in data_name:
    print(f'    {key}, {list(value)}')