class Employee:
    def hello_emp(self,Name=None):
        if Name is not None:
            print("Hello "+Name)
        else:
            print("Hello")

e1 = Employee()
e1.hello_emp("Shravan")
e1.hello_emp()