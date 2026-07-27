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

    
