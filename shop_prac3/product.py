# 2026 07 21
class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = "active"

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
