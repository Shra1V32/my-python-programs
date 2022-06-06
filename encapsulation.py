class Base:
    def __init__(self):
        self._a = 2
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self._a)
        self._a = 3
        print(self._a)

d1 = Derived()