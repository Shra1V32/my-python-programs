terms = int(input("Enter number of terms: "))
n1,n2 = 0,1
count = 0
if terms <=0:
    print("Please enter a positive integer")
elif terms==1:
    print(f"Fibonacci Sequence upto: {terms}: ")
    print(n1)
else:
    print("Fibonacci Sequence: ")
    while count<terms:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1