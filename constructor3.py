class Constructor2:
    def __init__(self,name,rollno):
        print("Parametrical constructor")
        self.name = name
        self.rollno = rollno
    def display2(self):
        print(self.name)
        print(self.rollno)
c2 = Constructor2('pqr',2)
c2.display2()