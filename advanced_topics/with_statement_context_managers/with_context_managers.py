class Manager():
    def __enter__(self):
        print('Entering context manager')
        return 'could be a object like a connection DB, etc'
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('Exiting')
        print(f'Execeptions: {exc_type}, {exc_value}, {traceback}')


with Manager() as manager:
    print(f'Is a string but {manager}' )