class Employee:
    def __init__(s,name,eid,desg,sal):
        s.name = name
        s.eid = eid
        s.desg = desg
        s.sal = sal
    def display(s):
        print(s.name)
        print(s.eid)
        print(s.desg)
        print(s.sal)
emp1 = Employee('Shravan',1,'CEO',100000)
emp2 = Employee('ZYZ',2,'Hello',100)

emp1.display()
emp2.display()