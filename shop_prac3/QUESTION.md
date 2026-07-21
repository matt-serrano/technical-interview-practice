# Technical Interview Practice: Inventory and Order System

Design and implement a small object-oriented inventory system for an online shop.

Create your solution inside this directory using Python. Your design must contain at least the two classes described below. You may add helper methods or classes if you think they improve the design.

## `Product`

A product has:

- a unique product ID
- a name
- a price
- a quantity currently in stock
- a status of `active` or `discontinued`

New products are `active` by default.

Implement behavior that allows callers to:

- read the product's ID, name, price, stock quantity, and status
- add a positive quantity of stock
- remove a positive quantity of stock, but never more than is available
- discontinue a product

Invalid operations must fail without changing the product. For example, adding zero items or removing more items than are in stock must not modify the stock quantity. A discontinued product cannot have stock added or removed.

## `InventorySystem`

The inventory system manages products and customer orders.

Implement behavior that allows callers to:

- add a product, rejecting another product with the same product ID
- return all active products
- return all active products that currently have stock available
- look up a product by its product ID
- place an order containing one or more products and requested quantities

Each successful order must have a unique order ID and must be recorded by the system.

An order may be placed only when:

- the order contains at least one item
- every requested quantity is a positive integer
- every product is registered in the inventory system
- every product is active
- every product has enough stock for the requested quantity

Placing an order must be atomic: if any item in the order is invalid, the order fails, no stock quantities change, and no order is recorded. If the order succeeds, reduce the stock of every ordered product and record the order.

Choose a clear input format for an order (for example, a dictionary mapping product IDs to quantities) and document that choice in your code.

## Expected behavior examples

- Adding the same product ID twice fails, even if the two `Product` objects are different.
- A product with zero stock is active but is not considered available.
- Ordering two units from a product with five units leaves three units.
- An order requesting valid stock from one product and too much stock from another fails without reducing either product's stock.
- A discontinued product does not appear in active-product results and cannot be ordered.

## What to demonstrate

Write automated tests covering successful operations, invalid inputs, state changes, duplicate IDs, filtering, and the atomic-order rule. Keep the public interface consistent and make return values clear enough that callers can distinguish success from failure.
