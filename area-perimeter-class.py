import math
class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
r = int(input("Enter radius: "))
obj = circle(r)
print("area=",round(obj.area(),3))
print("Perimeter=",round(obj.perimeter(),3))