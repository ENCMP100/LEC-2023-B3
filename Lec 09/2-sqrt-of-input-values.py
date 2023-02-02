"""
Created on Wed Feb  1 20:57:37 2023

@author: ranaweer
"""
import numpy as np

# While loop continues as long as its test "condition" is True

# Example 1
# The following loop continues until you enter a negative number
num = float(input('Enter a number: '))
while num >= 0:
    # Calculate and print the square root
    print("Square root of", num, "is", np.sqrt(num))
    
    # Take the next number
    num = float(input('Enter a number: '))


# Example 2
# The following loop continues until you enter an empty string
num_string = input('Enter a number: ')
while num_string != "":
    num = float(num_string)
    # Calculate and print the square root
    print("Square root of", num, "is", np.sqrt(num))
    
    # Take the next number
    num_string = input('Enter a number: ')

