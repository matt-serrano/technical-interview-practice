# 2026 07 21
class Product:
    def __init__(self, id, name, price, quantity):
        self._id = id
        self._name = name
        self._price = price
        self._quantity = quantity
        self._status = "active"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    def product_information(self):
        return f"Product: {self.name}, ID: {self.id}, Price: {self.price}, Quantity: {self.quantity}, Status: {self.status}."
    
    def add_stock(self, amount):
        if self.status != "active":
            return False

        if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
            return False

        self.quantity += amount
        return True

    def remove_stock(self, amount):
        if self.status != "active":
            return False

        if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
            return False

        if amount > self.quantity:
            return False
        
        self.quantity -= amount
        return True
    
    def discontinue(self):
        self.status = "discontinued"
        return True
