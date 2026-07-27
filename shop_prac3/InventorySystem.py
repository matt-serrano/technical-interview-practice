from Product import Product

class InventorySystem:
    def __init__(self):
        self.products = []

    def lookup_product(self, product_id):
        for i in self.products:
            if i.id == product_id:
                return True

        return False

    def add_product(self, product):
        if self.lookup_product(product.id) is not None:
            return f"Cannot add existing product!"

        self.products.append(product)
        return f"Adding {product.product_information()} to inventory system!"

    def active_products(self):
        active = []
        for i in self.products:
            if i.status == "active":
                active.append(i)

        return active

    def active_products_stock(self):
        active = self.active_products()

        for i in range(len(active)):
            if i.quantity <= 0:
                active.pop(i)

        return active

    
