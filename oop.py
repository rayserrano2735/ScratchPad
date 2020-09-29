class Car:
    def __init__(self , color, make, mileage):
        self.color = color
        self.make = make
        self.mileage = mileage
        
    def __str__(self):
        return f"This car is a {self.color} {self.make} with {self.mileage} miles"