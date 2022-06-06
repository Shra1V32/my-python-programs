class Parent:
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln
    def print_name(self):
        print(self.fname,self.lname)
class Child(Parent):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.branch = 'IT'
        self.year = 1
x = Child("ABC","XYZ")
x.print_name()
print(x.branch,x.year)
