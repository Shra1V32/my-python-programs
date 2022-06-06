def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))

terms = int(input("Enter a number: "))

if terms <= 0:
    print("Enter a postive integer")
else:
    print("Fibonacci Sequence")
    for i in range(terms):
        print(fib(i))