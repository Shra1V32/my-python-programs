class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
n = input("Enter name: ")
r = int(input("Enter roll no: "))
p1=student(n,r)
print(p1.name)
print(p1.rollno)