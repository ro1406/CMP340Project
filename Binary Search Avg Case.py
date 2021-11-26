# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 02:31:02 2021

@author: rohan
"""
import time
import math
import matplotlib.pyplot as plt
import numpy as np

def binarySearch(arr, l, r, x):
    counter=0
    while l <= r:
       	mid = int((l+r) / 2)+1;
        counter+=1
       	if arr[mid] == x:
             	return counter
       	elif arr[mid] < x:
           	l = mid + 1
       	else:
           	r = mid - 1        
    return -1

t0=time.time()

sizes=[]
ops=[]
for i in range(1,1000+1): # 1*10^5 to 1000 *10^5 Elements
    arr=np.arange(1,i*100000+1) # Faster than using list compehensions
    l,r=0,i*100000
    #Try to search for 10 random values, and average the counts:
    total=0
    for j in range(10):
        x=np.random.randint(1,i*100000+1)
        total+=binarySearch(arr,l,r,x)
    t=total/10
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

myfile=open("BS 100M every 100K Avg Case - Smooth.csv",'w')
for i in range(len(ops)):
    myfile.write(str(sizes[i])+","+str(ops[i])+"\n")
myfile.close()
