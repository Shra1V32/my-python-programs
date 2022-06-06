#Factorial of a given number (Without recursion)
n = int(input("Enter your number: "))
f=1
if n<0:
    print("Factorial doesn't exist for negative number")
elif n==0:
    print("The factorial of " + str(n) +" is 1")
else:
    for i in range(1,n+1):
        f*=i
    print("The factorial of " + str(n) +" is " + str(f))