a = []
n = int(input("Enter the number of elements in the list: "))

for x in range(0,n):
    element=input("Enter element" + str(x+1)+":")
    a.append(element)
print(a)
c=[]

count=0
b = input("Enter your word to remove: ")
n = int(input("Enter the occurence to remove: "))

for i in a:
    if i==b:
        count+=1
        if count!=n:
            c.append(i)
    else:
        c.append(i)
if count==0:
    print("Item not found")
else:
    print("The number of repetitions is: ",count)
    print("Updated list is: ",c)