items = [1,6,7,7,67,23,5,3,2,4,9,12,45,75]
x = int(input("Enter a value: "))
c = items.count(x)
print(c)

# Counting number of occurences using for loop
count=0
for item in items:
    if item == 7:
        count+=1
print(count)
counts = {}
for item in items:
    if item in counts:
        counts[item]+= 1
    else:
        counts[item]=1
print(counts.get(x))
