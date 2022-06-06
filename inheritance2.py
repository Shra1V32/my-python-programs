class Parent:
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln
    def print_name(self):
        print(self.fname,self.lname)
class Child(Parent):
    def __init__(self,fn1,ln1):
        Parent.__init__(self,fn1,ln1)

x = Child("Shiva","Maram")
x.print_name()
