k = input("Enter your 3-digit number: ")

com=[]

for i in k:
    com.append(int(i))

for j in range(0,3):
    for w in range(0,3):
        for l in range(0,3):
            if j!=w and w!=l and l!=j:
                print(com[j],com[w],com[l])