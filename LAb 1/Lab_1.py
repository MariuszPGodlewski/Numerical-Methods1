import numpy as np
import math
import time

A = np.random.rand(1000, 1000)
B = np.random.rand(1000, 1000)
c = np.random.rand(1000)

print("Shape of A:", A.shape)
print("Shape of B:", B.shape)
print("Shape of c:", c.shape)
print("Memory usage:", A.nbytes)
#print("Memory usage in MB:", A.nbytes / (1024 * 1024))
n = math.sqrt(32*1024*1024*1024/8)
print("The biggest square matrix in 32 GB RAM memory: ",n,"x",n  )

time_start = time.time()
A = np.random.rand(5000, 5000)
B = np.random.rand(5000, 5000)
c = np.random.rand(5000)
A@B@c

time_end= time.time()
print(time_end - time_start)

time_start = time.time()
A = np.random.rand(5000, 5000)
B = np.random.rand(5000, 5000)
c = np.random.rand(5000)
A@(B@c)

time_end= time.time()
print(time_end - time_start)
