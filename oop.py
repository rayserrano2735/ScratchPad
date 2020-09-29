# Car class
class Car:
    def __init__(self, color, make, mileage):
        self.color = color
        self.make = make
        self.mileage = mileage

    def __str__(self):
        return f"This car is a {self.color} {self.make} with {self.mileage} miles"

    def show_model(self, model):
        return f'This {self.make} is a {model}'


class FordCar(Car):
    def show_model(self, model='Mustang'):
        return super().show_model(model)


