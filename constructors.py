class Student:
    count = 0
    def __init__(self):
        Student.count+=1
s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()
s5 = Student()
s6 = Student()

print(Student.count)