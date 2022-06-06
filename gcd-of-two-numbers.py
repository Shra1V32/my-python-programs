def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x

n1=int(input("Enter your first number: "))
n2=int(input("Enter your second number: "))
print("GCD is: ",gcd(n1,n2))