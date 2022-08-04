import sys
n = len(sys.argv)
if n==1:
    print("No arguments passed")
else:
    sum = 0
    for i in sys.argv[1:]:
        sum=int(i)+sum
    print(f"Sum of the numbers passed through args is: {sum}")

