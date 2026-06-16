from car import Car
from datetime import datetime, date

class RentalSystem:
    def __init__(self):
        self.list_of_cars = []
        self.rented_cars = {}

    def add_car_to_list(self, car):
        if car not in self.list_of_cars:
            self.list_of_cars.append(car)
            return True
        return False
    
    def get_available_cars(self):
        available_cars = []
        for car in self.list_of_cars:
            if car.get_status() == "available":
                available_cars.append(car)
        return available_cars
    
    def _dates_overlap(self, start1, end1, start2, end2):
        if isinstance(start1, str):
            start1 = datetime.strptime(start1, "%Y-%m-%d").date()
        if isinstance(end1, str):
            end1 = datetime.strptime(end1, "%Y-%m-%d").date()
        if isinstance(start2, str):
            start2 = datetime.strptime(start2, "%Y-%m-%d").date()
        if isinstance(end2, str):
            end2 = datetime.strptime(end2, "%Y-%m-%d").date()
        return start1 <= end2 and start2 <= end1
    
    def rent(self, car, start_date, end_date):
        if car in self.rented_cars:
            existing_start, existing_end = self.rented_cars[car]
            if self._dates_overlap(start_date, end_date, existing_start, existing_end):
                return False
        if car.get_status() == "available":
            self.rented_cars[car] = (start_date, end_date)
            return car.rent()
        return False    
