"""
Created on Tue Feb  7 14:33:03 2023

@author: ranaweer
"""

is_int = False
while not is_int:
    input_str = input("Enter an integer: ")
    
    is_int = True
    for c in input_str:
        if not (c>='0' and c <='9'):
            is_int = False;
            break # breaking for c in input_str


print("The number you entered is", int(input_str))

