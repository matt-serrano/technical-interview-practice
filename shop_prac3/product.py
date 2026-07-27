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
        if amount <= 0:
            return f"Cannot remove 0 or less items!"

        self.quantity += amount
        return f"{amount} added to {self.name} stock. New quantity is {self.quantity}."

    def remove_stock(self, amount):
        if self.stock <= 0 or amount > self.stock:
            return f"Not enough products!"

        if amount <= 0:
            return f"Cannot remove 0 or less items!"
        
        self.quantity -= amount
        return f"{amount} added to {self.name} stock. New quantity is {self.quantity}."
    
    def discontinue(self):
        answer = input(f"Are you sure you would like to discontinue {self.product}? (y/n) ")

        if answer == "y":
            self.status = "discontinued"
            return f"{self.name} has been discontinued!"
        else:
            return f"No changes have been made! {self.name} is still active!"
