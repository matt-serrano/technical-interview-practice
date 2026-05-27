class Car:
    def __init__(self, make, model, price, year):
        self._make = make
        self._model = model
        self._year = year
        self._status = "available"

    def get_make(self):
        return self._make
    
    def get_model(self):
        return self._model

    def get_year(self):
        return self._year
    
    def get_status(self):
        return self._status
    
    def rent(self):
        if self._status == "available":
            self._status = "unavailable"
            return True
        return False
    
    def return_car(self):
        if self._status == "unavailable":
            self._status = "unavailable"
            return True
        return False