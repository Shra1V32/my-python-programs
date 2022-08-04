a = []

ran = int(input('Enter the number of elements in the list: '))
for i in range(1,ran+1):
    element = input(f"Enter {i+1} Element: ")
    a.append(element)
max=len(a[0])
word=a[0]
for i in a:
    if len(i)>max:
        max=len(i)
        temp = i

print("The word with the longest length is: ",temp)