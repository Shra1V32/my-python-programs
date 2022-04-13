s=0
n=int(input("Enter your number: "))
temp=n
while (n):
    i=1
    f=1
    r=n%10
    while(i<=r):
        f=f*i
        i=i+1
    s=s+f
    n=n//10
if s==temp:
    print("Number is a strong number")
else:
    print("Number is not a strong number")
