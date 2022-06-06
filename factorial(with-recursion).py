#Factorial using recursion
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

num = int(input("Enter your number: "))

if num<0:
    print("Factorial for negative number doen't exist.")
elif num == 0:
    print("The factorial 0 is 1")
else:
    print("The factorial of",num,"is",factorial(num))