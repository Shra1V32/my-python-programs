from xml.dom.minidom import Element


a=[]
n=int(input("Enter the number of elements in the list: "))
for x in range(0,n):
    element = input(f"Enter element {x+1}: ")
    a.append(element)
print(a)
c=[]
count=0
b = input("Enter word to remove: ")
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
    print(f"The number of repetetions are: {count}")
    print(f"Updated list is {c}")
