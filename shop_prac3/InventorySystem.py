class InventorySystem:
    def __init__(self):
        self.products = []
        self.orders = []
        self._next_order_id = 1

    def lookup_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product

        return None

    def add_product(self, product):
        if self.lookup_product(product.id) is not None:
            return "Cannot add existing product!"

        self.products.append(product)
        return f"Adding {product.product_information()} to inventory system!"

    def get_active_products(self):
        return [
            product
            for product in self.products
            if product.status == "active"
        ]

    def active_products(self):
        return self.get_active_products()

    def get_available_products(self):
        return [
            product
            for product in self.get_active_products()
            if product.quantity > 0
        ]

    def active_products_stock(self):
        return self.get_available_products()

    def place_order(self, items):
        """Place an order from a dictionary of {product_id: quantity}."""
        if not isinstance(items, dict) or not items:
            return "Order must contain at least one item."

        products_to_update = []

        # Validate the complete order before changing any stock.
        for product_id, quantity in items.items():
            if (
                not isinstance(quantity, int)
                or isinstance(quantity, bool)
                or quantity <= 0
            ):
                return "Every requested quantity must be a positive integer."

            product = self.lookup_product(product_id)
            if product is None:
                return f"Product {product_id} is not registered."
            if product.status != "active":
                return f"Product {product_id} is discontinued."
            if product.quantity < quantity:
                return f"Product {product_id} has insufficient stock."

            products_to_update.append((product, quantity))

        for product, quantity in products_to_update:
            product.remove_stock(quantity)

        order = {
            "order_id": self._next_order_id,
            "items": items.copy(),
        }
        self.orders.append(order)
        self._next_order_id += 1
        return order
