arr=[]
ams=0
num = input("Enter the number: ")

if num!=int(num):
    pass
for i in num:
    arr.append(int(i))
for j in arr:
    ams+=j**3

num=int(num)
if num==ams:
    print("The given number is an ams num")
else:
    print("The given number is not an ams number")

