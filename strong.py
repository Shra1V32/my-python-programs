def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
num = input("Enter your number: ")
if num != int(num):
    pass
arr = []
strong = 0
for i in num:
    arr.append(int(i))
for j in arr:
    strong += fact(j)
if strong == int(num):
    print("This is a strong number")
else:
    print("This is not a strong number")
