from oop import  Car, FordCar
any_car = Car(color='White', mileage = '100', make= 'Toyota')
ford_car = FordCar('Black', 'Ford', '10000')
print(any_car)
print(ford_car)
print(any_car.show_model('Corolla'))
print(ford_car.show_model())