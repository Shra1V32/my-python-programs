class Error(Exception):
    pass
class SmallValueError(Error):
    pass
class LargeValueError(Error):
    pass
n = 10

while True:
    try:
        i = int(input("Enter a number:"))
        if i<n:
            raise SmallValueError
        if i>n:
            raise LargeValueError
        break
    except SmallValueError:
        print("Value is too small")
    except LargeValueError:
        print("Value is too large")
print("You have guessed correct answer")