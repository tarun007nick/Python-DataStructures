import time

'''
def min_num():
    n = input("Total numbers you want to enter")
    value = []
    
    while n != 0:
        x = input("enter the numbers")
        value.append(x)
        
    for i in len(value):
        if value[i] < value[i+1]:
            min_number = value[i]
            i+1
        else
            min_number = value[i+1]
'''
from random import randrange

# Function to calculate time taken in finding min number in O(n^2) 
def findmin(alist):
    overallmin = alist[0]
    print(overallmin)
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i 
    return overallmin

#print(findmin([2,4,1,7,4,0]))

# Function to calculate time taken in finding min number in O(n)
def leastnumber(aList):
    min_num = aList[0]
    for i in aList:
        if i < min_num:
            min_num = i
    return min_num
  

#print(leastnumber([2,4,1,7,4,0]))      

#To find time in case of O(n)
for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(leastnumber(alist))
    end = time.time()
    print("size: %d time: %f" % (listSize,end-start))
       
#To find time in case of O(n^2)
for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findmin(alist))
    end = time.time()
    print("size: %d time: %f" % (listSize,end-start))