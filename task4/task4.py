import sys
import os
import datetime
import time

file = open("intervals.txt")
intervals = []
for line in file:
    intervals.append([(x) for x in line.split()])
file.close()

def findIntersection(interval,N): 
  
    l = intervals[0][0] 
    r = intervals[0][1] 
  
    for i in range(1,N): 
        if (intervals[i][0] < r or intervals[i][1] > l): 
            l = max(l, intervals[i][0]) 
            r = min(r, intervals[i][1])      
  
    print("[",l,", ",r,"]") 
    
N =len(intervals) 
findIntersection(intervals, N) 




