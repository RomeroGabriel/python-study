print('Starting BUILT-IN FUNCTIONS!!!!')
print()

print('all(iterable)')
all_true = [True for _ in range(0, 3)]
print(f'\tsimple1: {all(all_true)}, all_true values {all_true}')
not_all_true = all_true + [False]
print(f'\tsimple2: {all(not_all_true)}, not_all_true values {not_all_true}')
print('\twith "lambda functions"')
print(f'\tall bigger than 0: {all(isinstance(e, int) and e > 0 for e in all_true )}')
print(f'\tnot all bigger than 0: {all(isinstance(e, int) and e > 0 for e in not_all_true )}')

print()
print('any(iterable)')
print('SAME THING THAT ALL FUNCTIONS')

