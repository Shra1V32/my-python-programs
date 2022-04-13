# Amstrong number
num=int(input("Enter your number: "))
ams=0
actual_num=num
while num!=0:
    tmp=num%10
    ams+=tmp**3
    num//=10
if ams!=actual_num:
    print("Number isn't an amstrong number")
else:
    print("Number is an amstrong number")