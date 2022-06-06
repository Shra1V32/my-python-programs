class Base:
    def __init__(self):
        self.a = 'mvsrec'
        self._c = 'IT'
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self._c)
d = Derived()