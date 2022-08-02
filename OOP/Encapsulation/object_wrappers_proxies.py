class Holding():
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __setattr__(self, __name: str, __value):
        if __name not in { 'name', 'date', 'shares', 'price' }:
            raise AttributeError(f'No Attribute {__name}')
        super().__setattr__(__name, __value)

    def __getattr__(self, __name: str):
        # Failsafe. Only called for missing attributes
        print(f'No value {__name}')

    def cost(self):
        return self.shares * self.price

holding = Holding('Test', '2022-08-02', 10, 100.00)
print(holding.test)

try:
    holding.test = 123
except Exception as e:
    print(e)


# Proxie class
class Readonly():
    def __init__(self, obj):
        self._obj = obj
    
    def __setattr__(self, __name: str, __value):
        if __name == '_obj':
            super().__setattr__(__name, __value)
        else:
            raise AttributeError(f'Read only')

    def __getattr__(self, __name: str):
        return getattr(self._obj, __name)

p = Readonly(holding)
print(f'Read P: {p.name}')
print(f'Read P: {p.date}')
try:
    p.test = 123
except Exception as e:
    print(f'Read only object working: {e}')