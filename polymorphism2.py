class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        print(self.name)
        print(self.color)
        print(self.price)
    def max_speed(self):
        print("Max Speed is 100 kmph")
    def change_gear(self):
        print("Vehicle has 6 gears")

class Car(Vehicle):
    def max_speed(self):
        print("Max Speed of car is 200 Kmph")
    def change_gear(self):
        print("Car has 8 gears")
c1 = Car('Benz','Green','20000')
c1.show()
c1.max_speed()
c1.change_gear()