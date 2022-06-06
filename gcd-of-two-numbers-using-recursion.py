def gcd(a,b):
    if a==b:
        return a
    elif a<b:
        return gcd(b,a)
    else:
        return gcd(b,a-b)
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print(gcd(a,b))