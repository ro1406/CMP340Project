# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 00:14:10 2021

@author: rohan
"""
import time
import math
import matplotlib.pyplot as plt
import numpy as np

def interpolationSearch(arr, term):
    count = 0
    n = len(arr) - 1
    l = 0
    r = n

    while l <= r:
        
        mid = l + int((r - l) * (term - arr[l]) // (arr[r] - arr[l]))
        
        if mid > r or mid < l:
            return count+1

        if arr[mid] == term:
            return count+1

        if term > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
        count += 1
    if l > r:
        return count+1

t0=time.time()
sizes=[]
ops=[]
MAGNITUDE=int(1e4)
for i in range(1,100+1): # 1*10^4 to 100 *10^4 Elements
    arr=[x**8 for x in range(1,i*MAGNITUDE+1)]
    #print("Len(arr)=",len(arr))
    #arr[-1]*=10000
    #Try to search for 10 random values, and average the counts:
    total=0
    for j in range(1000):
        x=np.random.randint(1,i*MAGNITUDE+1)
        total+=interpolationSearch(arr,x)
    t=total/1000
    ops.append(t)
    sizes.append(i)
    del arr #Memory reasons

t=time.time()-t0
print("Testing done! Time Taken:",t)

log=lambda x:math.log(math.log(x+1,2),2)
logGraph=np.vectorize(log)(np.arange(1,int(1e6),MAGNITUDE))

plt.plot(sizes,ops,'r')
plt.xlabel("Size of array (n) *10^4")
plt.ylabel("Number of operations")
plt.title("Size of array VS. Num operations")
plt.show()

plt.plot(sizes,ops,'r')
plt.plot(logGraph,'b')
plt.legend(['Experimental','Theoretical'])
plt.xlabel("Size of array (n) *10^4")
plt.ylabel("Number of operations")
plt.title("Size of array VS. Num operations")
plt.show()

myfile=open("IS 1M every 10K Avg Case - Smooth.csv",'w')
for i in range(len(ops)):
    myfile.write(str(sizes[i])+","+str(ops[i])+"\n")
myfile.close()
