class Integer():
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        instance.__dict__[self.name] = value

class Point():
    # value NEEDS to be in class level
    # can't be in init
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x , y):
        self.x = x
        self.y = y