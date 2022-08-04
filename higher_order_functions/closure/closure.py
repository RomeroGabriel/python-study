print('Starting with CLOSURE!!!')

print('Accessing a non-local variable in a nested function')

def print_msg(msg='Non-local variables being printed in a nested function'):
    def printer():
        print()
        print('Nested function!!!')
        print(f'    Non-local msg: {msg}')
        print()
    printer()

print_msg()

print('But to be a closure is necessary to return the nested function')
print('So...')

def print_msg_closure(msg='now this is a closure'):
    def printer_closure():
        print()
        print('Nested function!!!')
        print(f'    Non-local msg: {msg}')
        print()
    return printer_closure

closure_var = print_msg_closure()
print(f'Now we can store the funtion to be executed in another time. {type(closure_var)}')
closure_var()