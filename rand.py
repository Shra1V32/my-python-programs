import random

A = random.randint(0,500)
B = random.randint(45,500)

print(f"Q: What is {A} + {B} ?")
resp = int(input("Enter your answer: "))

if resp!=A+B:
    print("Wrong answer")
else:
    print("Right Answer")