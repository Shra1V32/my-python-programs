first=int(input("Enter your first number: "))
second=int(input("Enter your second number: "))
third=int(input("Enter your third number: "))
list1=[]
list1.append(first)
list1.append(second)
list1.append(third)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i!=j & j!=k & k!=i):
                print(list1[i],list1[j],list1[k])