import sys
import os
import numpy as np

file = open(sys.argv[1])

K = []
for line in file:
    K.append(int(line))
file.close()

if len(K)>1000:
    print("Число строк превысило допусимое значение 1000")
    sys.exit()
    
percentile = np.percentile(K, 90)
mediana = np.median(K)
maxK = max(K)
minK = min(K)
mean = np.mean(K)

print("{:.2f}".format(percentile))
          
print("{:.2f}".format(mediana))

print("{:.2f}".format(maxK))

print("{:.2f}".format(minK))

print("{:.2f}".format(mean))

