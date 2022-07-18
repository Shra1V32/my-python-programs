s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
#a = list(set(s1)-set(s2))
#print("Letters present only in string1: ")
#for i in a:
#    print(i)
for i in s1:
    for j in s2:
        if i==j:
            s1=s1.replace(i,"")
for i in s1:
    print(i,end='\n')
