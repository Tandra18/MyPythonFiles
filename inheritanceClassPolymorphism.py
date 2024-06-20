class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    def move(self):
        print("Drive")

class Boat(Vehicle):
    pass

class Plane(Vehicle):
    def move(self):
        print("Fly")

car1 = Car("Ford","Mustang")
boat1 = Boat("Titanic","Touring")
plane1 = Plane("Panam","445")

for x in (car1,boat1,plane1):
    x.move()
