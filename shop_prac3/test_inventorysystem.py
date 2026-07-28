import unittest

from InventorySystem import InventorySystem
from Product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "Keyboard", 50, 5)

    def test_new_product_is_active(self):
        self.assertEqual(self.product.status, "active")
        self.assertNotEqual(self.product.status, "discontinued")

    def test_product_information_can_be_read(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, "Keyboard")
        self.assertEqual(self.product.price, 50)
        self.assertEqual(self.product.quantity, 5)

    def test_add_stock_increases_quantity(self):
        self.assertTrue(self.product.add_stock(3))
        self.assertEqual(self.product.quantity, 8)

    def test_add_invalid_stock_does_not_change_quantity(self):
        self.assertFalse(self.product.add_stock(0))
        self.assertEqual(self.product.quantity, 5)

    def test_remove_stock_decreases_quantity(self):
        self.assertTrue(self.product.remove_stock(2))
        self.assertEqual(self.product.quantity, 3)

    def test_remove_too_much_stock_does_not_change_quantity(self):
        self.assertFalse(self.product.remove_stock(6))
        self.assertEqual(self.product.quantity, 5)

    def test_discontinued_product_cannot_change_stock(self):
        self.product.discontinue()

        self.assertFalse(self.product.add_stock(1))
        self.assertFalse(self.product.remove_stock(1))
        self.assertEqual(self.product.quantity, 5)


class TestInventorySystem(unittest.TestCase):
    def setUp(self):
        self.system = InventorySystem()
        self.keyboard = Product(1, "Keyboard", 50, 5)
        self.mouse = Product(2, "Mouse", 25, 2)

    def test_add_product_and_lookup_by_id(self):
        self.system.add_product(self.keyboard)

        self.assertIs(self.system.lookup_product(1), self.keyboard)
        self.assertIsNone(self.system.lookup_product(999))

    def test_add_product_rejects_duplicate_id(self):
        duplicate = Product(1, "Different keyboard", 75, 10)

        self.system.add_product(self.keyboard)
        self.system.add_product(duplicate)

        self.assertEqual(self.system.products, [self.keyboard])

    def test_get_active_products_excludes_discontinued_products(self):
        self.mouse.discontinue()
        self.system.add_product(self.keyboard)
        self.system.add_product(self.mouse)

        self.assertEqual(self.system.get_active_products(), [self.keyboard])

    def test_get_available_products_excludes_zero_stock(self):
        empty_product = Product(3, "Webcam", 80, 0)
        self.system.add_product(self.keyboard)
        self.system.add_product(empty_product)

        self.assertEqual(self.system.get_available_products(), [self.keyboard])

    def test_successful_order_reduces_stock_and_is_recorded(self):
        self.system.add_product(self.keyboard)
        self.system.add_product(self.mouse)

        order = self.system.place_order({1: 2, 2: 1})

        self.assertEqual(order["order_id"], 1)
        self.assertEqual(order["items"], {1: 2, 2: 1})
        self.assertEqual(self.keyboard.quantity, 3)
        self.assertEqual(self.mouse.quantity, 1)
        self.assertEqual(self.system.orders, [order])

    def test_successful_orders_receive_unique_ids(self):
        self.system.add_product(self.keyboard)

        first_order = self.system.place_order({1: 1})
        second_order = self.system.place_order({1: 1})

        self.assertEqual(first_order["order_id"], 1)
        self.assertEqual(second_order["order_id"], 2)

    def test_empty_order_fails(self):
        result = self.system.place_order({})

        self.assertIsInstance(result, str)
        self.assertEqual(self.system.orders, [])

    def test_invalid_quantity_fails_without_changing_stock(self):
        self.system.add_product(self.keyboard)

        result = self.system.place_order({1: 0})

        self.assertIsInstance(result, str)
        self.assertEqual(self.keyboard.quantity, 5)
        self.assertEqual(self.system.orders, [])

    def test_unknown_product_fails_without_changing_stock(self):
        self.system.add_product(self.keyboard)

        result = self.system.place_order({1: 2, 999: 1})

        self.assertIsInstance(result, str)
        self.assertEqual(self.keyboard.quantity, 5)
        self.assertEqual(self.system.orders, [])

    def test_discontinued_product_cannot_be_ordered(self):
        self.keyboard.discontinue()
        self.system.add_product(self.keyboard)

        result = self.system.place_order({1: 1})

        self.assertIsInstance(result, str)
        self.assertEqual(self.keyboard.quantity, 5)
        self.assertEqual(self.system.orders, [])

    def test_order_is_atomic_when_one_product_has_insufficient_stock(self):
        self.system.add_product(self.keyboard)
        self.system.add_product(self.mouse)

        result = self.system.place_order({1: 2, 2: 3})

        self.assertIsInstance(result, str)
        self.assertEqual(self.keyboard.quantity, 5)
        self.assertEqual(self.mouse.quantity, 2)
        self.assertEqual(self.system.orders, [])


if __name__ == "__main__":
    unittest.main()
