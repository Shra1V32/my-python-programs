# Check whether the given date is valid or not
date = input("Enter your date in DD-MM-YYYY Format: ")
d,m,y = date.split('-')
d = int(d)
m = int(m)
y= int(y)
#if d > 31 or m > 12 or d < 0 or m < 0:
 #   print("Invalid date")
#elif m==2 and d>\
if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    days=31
elif (m==4 or m==6 or m==9 or m==11):
    days=30
elif (y%4 == 0 and y %100 != 0 or y%400 == 0):
    days=29
else:
    days=28
# To check whether the given date is valid
if (m<1 or m>12 or d>31 or d<1 or d>days):
    print("Invalid date")
elif (d==days and m==12):
    d=1
    m=1
    y=y+1
    print("Incremented date: ",d,m,y)
else:
    d=d+1
    print("Incremented date: ",d,"-",m,"-",y)

