import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius

r=int(input("Enter the radius: "))
obj = Circle(r)
print(f"Area: {round(obj.area(),4)}")
print(f"Perimeter: {round(obj.perimeter(),4)}")
