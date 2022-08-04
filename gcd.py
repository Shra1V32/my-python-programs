def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x

A = int(input("Enter your first number: "))
B = int(input("Enter your second number: "))
print("GCD is",gcd(A,B))