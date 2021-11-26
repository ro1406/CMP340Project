# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 03:05:40 2021

@author: rohan
"""
import time
import math
import matplotlib.pyplot as plt
import numpy as np
def interpolationSearch(arr, lo, hi, x,count=0):
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))
 
        # Condition of target found
        if arr[pos] == x:
            return count #pos
 
        # If x is larger, x is in right subarray
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1, hi, x,count+1)
 
        # If x is smaller, x is in left subarray
        if arr[pos] > x:
            return interpolationSearch(arr, lo, pos - 1, x,count+1)
    return -1


t0=time.time()

sizes=[]
ops=[]
for i in range(1,1000+1): # 1*10^5 to 1000 *10^5 Elements
    arr=np.arange(1,i*100000+1) # Faster than using list compehensions
    l,r=0,i*100000-1
    x=2                       #int(len(arr)/(math.floor(math.log(len(arr),2))+1))
    t=interpolationSearch(arr,l,r,x)
    ops.append(t)
    sizes.append(i)
    del arr #Memory reasons

t=time.time()-t0
print("Testing done! Time Taken:",t)

log=lambda x:math.log(x,2)
logGraph=np.vectorize(log)(np.arange(1,int(1e8),100000))


plt.plot(sizes,ops,'r')
plt.plot(logGraph,'b')
plt.legend(['Experimental','Theoretical'])
plt.xlabel("Size of array (n) *10^5")
plt.ylabel("Number of operations")
plt.title("Size of array VS. Num operations")
plt.show()

myfile=open("IS 100M every 100K - Smooth.csv",'w')
for i in range(len(ops)):
    myfile.write(str(sizes[i])+","+str(ops[i])+"\n")
myfile.close()