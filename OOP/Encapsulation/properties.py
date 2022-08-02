class Holding():
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, newprice):
        # encapsulate value to be float, can add validations
        if not isinstance(newprice, float):
            raise TypeError('Expected float')
        self._price = newprice

    @property # can be used also in functions to behave like property
    def cost(self):
        return self.shares * self.price


holding = Holding('Test', '2022-08-02', 10, 100.00)
print(holding.price)
try:
    holding.price = 4
except Exception as e:
    print(f'    Error trying to set price as integer: {e}')