import unittest
from datetime import date

from car import Car
from rentalsystem import RentalSystem


class TestRentalSystem(unittest.TestCase):
    def setUp(self):
        self.system = RentalSystem()
        self.car = Car("Toyota", "Corolla", 50, 2022)

    def test_add_car_to_list_adds_new_car_once(self):
        self.assertTrue(self.system.add_car_to_list(self.car))
        self.assertFalse(self.system.add_car_to_list(self.car))
        self.assertEqual(self.system.list_of_cars, [self.car])

    def test_get_available_cars_only_returns_available_cars(self):
        rented_car = Car("Honda", "Civic", 45, 2021)
        rented_car.rent()

        self.system.add_car_to_list(self.car)
        self.system.add_car_to_list(rented_car)

        self.assertEqual(self.system.get_available_cars(), [self.car])

    def test_rent_available_car_records_dates_and_marks_unavailable(self):
        self.system.add_car_to_list(self.car)

        self.assertTrue(self.system.rent(self.car, "2026-07-01", "2026-07-05"))
        self.assertEqual(self.car.get_status(), "unavailable")
        self.assertEqual(
            self.system.rented_cars[self.car],
            ("2026-07-01", "2026-07-05"),
        )

    def test_rent_unavailable_car_returns_false(self):
        self.car.rent()

        self.assertFalse(self.system.rent(self.car, "2026-07-01", "2026-07-05"))

    def test_dates_overlap_handles_string_and_date_values(self):
        self.assertTrue(
            self.system._dates_overlap(
                "2026-07-01",
                "2026-07-05",
                date(2026, 7, 4),
                date(2026, 7, 8),
            )
        )
        self.assertFalse(
            self.system._dates_overlap(
                "2026-07-01",
                "2026-07-05",
                date(2026, 7, 6),
                date(2026, 7, 8),
            )
        )

    def test_return_car_makes_car_available_again(self):
        self.car.rent()

        self.assertTrue(self.car.return_car())
        self.assertEqual(self.car.get_status(), "available")


def test_rental_system():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRentalSystem)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    assert result.wasSuccessful()


if __name__ == "__main__":
    test_rental_system()
