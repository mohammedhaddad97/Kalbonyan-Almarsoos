class Vehicle:
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.gas = 5
    
    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print('The {} {} goes VROOOOOOOM.'.format(self.color, self.manufacturer))
        else:
            print('The {} {} sputters out of gas.'.format(self.color, self.manufacturer))

class Car(Vehicle):
    def radio(self):
        print('Radio is on')
    
    def window(self):
        print('Windows are open')
    
class Motorcycle(Vehicle):
    def helmet(self):
        print('Helmet is on, you\'re safe!')

car = Car('blue', 'ferrari')
motor = Motorcycle('green', 'halawa')

car.drive()
car.drive()
car.drive()
motor.drive()
motor.drive()
car.window()
car.radio()
motor.helmet()
car.drive()
car.drive()
car.drive()
car.drive()
car.drive()