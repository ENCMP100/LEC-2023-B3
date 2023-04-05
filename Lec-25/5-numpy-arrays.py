## Arrays with Numpy

import numpy as np

array_1 = np.array([1, 5, 3, 7, 5])
array_2 = np.arange(5)
array_3 = np.arange(2, 7)
array_4 = np.arange(1, 3, 0.25)


one_d_array_of_zeros = np.zeros(5)
two_d_array_of_zeros = np.zeros((5,2))
three_d_array_of_zeros = np.zeros((5,2,3))

one_d_array_of_threes = np.full(5, 3)
two_d_array_of_threes = np.full((5,2), 3)


## Array reshaping
one_d = np.arange(12)
two_d = one_d.reshape((4,3))
three_d = one_d.reshape((2,3,2))


## VIEW: creates another view (different from referencing by assignment)

x3 = np.array([[1,2,3], 
               [4,5,6],
               [7,8,9]])

x3_a = x3; #Create a reference copy by assignment
x3_b = x3.view() # Create a shallow copy using the view function
print('x3.shape:', x3.shape)
print('x3_a.shape:', x3_a.shape)
print('x3_b.shape:', x3_b.shape)

# reshape x3 using shape property to be a 9x1 vector
x3.shape = 9,-1
print('x3.shape after reshaping x3:', x3.shape)
print('x3_a.shape after reshaping x3:', x3_a.shape) # NOTE: the shape of x3_a has change identical to x3
print('x3_b.shape after reshaping x3:', x3_b.shape) # NOTE: the shape of x3_b remains unchanged


## COPY: makes a deep copy of array data
x4 = np.arange(1,5) # a 5 element vector
x4_copy = x4.copy()

print('x4:', x4)
print('x4_copy:', x4_copy)

# Change the 3nd element inf x4 to 100
x4[1] = 100
print('x4 after changing x4:', x4)
print('x4_copy after changing x4:', x4_copy)



