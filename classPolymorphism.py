class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive")

class boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail")

class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")

car1 = car("ford","model")
boat1 = boat("titanic","touring")
plane1 = plane("AirAsia","455")

for x in (car1,boat1,plane1):
    x.move()