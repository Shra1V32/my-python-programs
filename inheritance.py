from curses import longname
from fnmatch import fnmatchcase
from re import L


class Parent:
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln
    def print_name(self):
        print(self.fname,self.lname)
class Child(Parent):
    pass
x = Child('Shravan','Vadeghar')
y = Child("Maram","Shiva Ganesh")
x.print_name()
y.print_name()
        