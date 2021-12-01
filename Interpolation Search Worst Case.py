# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 03:05:40 2021

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
graph=[0]

MAGNITUDE=int(1e5)

square=lambda x: math.pow(x,2)

for i in range(1,100+1): # 1*10^5 to 100 *10^5 Elements
    #arr=np.arange(1,i*MAGNITUDE+1,dtype='int64') # Faster than using list compehensions
    #arr=np.geomspace(1,i*MAGNITUDE,1000,dtype='int64')
    #arr=[x**2 for x in range(1,i*MAGNITUDE+1)]
    arr=np.vectorize(square)(np.arange(1,i*MAGNITUDE+1))
    #print("Len(arr)=",len(arr))
    arr[-1]*=10000
    graph.append(i*MAGNITUDE/10+30000)
    l,r=0,i*MAGNITUDE-1
    x=arr[-2]                   #int(len(arr)/(math.floor(math.log(len(arr),2))+1))
    t=interpolationSearch(arr,x)
    ops.append(t)
    sizes.append(i)
    del arr #Memory reasons

t=time.time()-t0
print("Testing done! Time Taken:",t)

log=lambda x:math.log(math.log(x+1,2),2)
logGraph=np.vectorize(log)(np.arange(1,int(1e8),MAGNITUDE))

plt.plot(sizes,ops,'r')
plt.xlabel(f"Size of array (n) *{MAGNITUDE}")
plt.ylabel("Number of operations")
plt.title("Size of array VS. Num operations EXPERIMENTAL")
plt.show()


plt.plot(sizes,ops,'r')
plt.plot(graph,'b')
plt.legend(['Experimental','Theoretical'])
plt.xlabel(f"Size of array (n) *10^5")
plt.ylabel("Number of operations")
plt.title("Size of array VS. Num operations")
plt.show()

myfile=open("IS 100M every 100K - Smooth.csv",'w')
for i in range(len(ops)):
    myfile.write(str(sizes[i])+","+str(ops[i])+"\n")
myfile.close()