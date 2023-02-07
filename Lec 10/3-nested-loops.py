#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:31:45 2023

@author: ranaweer
"""
print("E.g. 1")
for row in range(5):
    for col in range(4):
        print("*", end="")   
    print()
    
print("\nE.g. 2")
for row in range(1,5):
    for col in range(1, row+1):
        print("*", end="")   
    print()
