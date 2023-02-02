#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:14:59 2023

@author: ranaweer
"""

# FOR loops can be used to repeat a set of statements
# for a known number of times.

# Consider the following use of WHILE loop to print a given
# string one character at a time. 
# We have to use an index "i" to access characters of 
# the string and increment it in each iteration.

string_value = 'Alberta'
i = 0;
while i < len(string_value):
    print(string_value[i])
    i = i + 1
    

# Since we know we need to iterate the loop for each character,
# we cause a FOR loop as follows, which gives a simpler code.
print()
string_value = 'Alberta'
for letter in string_value:
    print(letter)
    
    
# Iterating through a range of values using a FOR loop

for n in range(1, 10):
    print(n)
    
odd_numbers = range(1, 10, 2)
for n in odd_numbers:
    print(n)

