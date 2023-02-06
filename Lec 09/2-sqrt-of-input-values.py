"""
Created on Wed Feb  1 20:57:37 2023

@author: ranaweer
"""
import numpy as np

"""
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
# The following loop continues until you enter an324 empty string
num_string = input('Enter a number: ')
while num_string != "":
    num = float(num_string)
    # Calculate and print the square root
    print("Square root of", num, "is", np.sqrt(num))
    
    # Take the next number
    num_string = input('Enter a number: ')

"""
# Example 3
# In this example, we set the condition of the while loop 
# to be True, so it will run as an infinite loop.
# Hwoever, when the user enters an empty input, we
# terminate the while loop by executing a 
# "break" statement.
while True:
    num_string = input('Enter a number: ')
    
    if num_string == "":
        break  # Break the loop, which skips the remaining 
               # steps in the loop and terminates the loop.
        
    num = float(num_string)
    # Calculate and print the square root
    print("Square root of", num, "is", np.sqrt(num))
    

print("Program ended!")
