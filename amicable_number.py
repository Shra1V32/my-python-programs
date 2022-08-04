from re import L


A = int(input("Enter your first number: "))
B = int(input("Enter your second number: "))

f1,f2 = 0,0

for i in range(1,A):
    if (A%i == 0):
        f1+=i
for j in range(1,B):
    if (B%j==0):
        f2+=j

if A==f2 and B==f1:
    print("They are amicable numbers")
else:
    print('They are not the amicable numbers')