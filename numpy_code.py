import numpy as np
#import pandas as pd
size = int(input('Enter your size of the array: '))
print("Enter",size,"Elements: ")
num=0
arr=[]
for i in range(size):
    item=int(input())
    arr.append(item)

npl=np.array(arr)
npl=npl.reshape(3,3)
print(npl)
print(np.sum(npl,axis=0)) # Rows
print(np.sum(npl))
print(np.sum(npl,axis=1)) # Columns
