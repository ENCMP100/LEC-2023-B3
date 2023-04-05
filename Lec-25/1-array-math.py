## Array Math

import numpy as np

array1 = np.arange(5)
cumsum1 = array1.cumsum()

array2 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

## CUMSUM: cumulative sum

print(array2)
print(array2.cumsum())

print(array2)
print(array2.cumsum(axis=0)) # cumulative sum along each column.

print(array2)
print(array2.cumsum(axis=1)) # cumulatieve sum along each row.


## DOT: dot product 

# with Rank 1  (1-D) arrays
x = np.array([2,3])
y = np.array([4,2])
print(np.dot(x,y)) # 2x4 + 3x2 = 14

# with Rank 2 (2D) arrays
x2 = np.array([[1,2,3],[4,5,6]]) 
y2 = np.array([[7,8],[9,10], [11,12]])
print(x2)
print(y2)

print(np.dot(x2,y2))


