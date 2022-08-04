import numpy as np
k = np.arange(6,12).reshape(3,2)
c = np.arange(15,21).reshape(2,3)
print(k)
#print(np.concatenate((k,c),axis=0))
k.sort(0)
print(k)