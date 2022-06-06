class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    def show(self):
        print(self.name)
        print(self.__salary)
c1 = Employee('ABC',1000)
c1.show()