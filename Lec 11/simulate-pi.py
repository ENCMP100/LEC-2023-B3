#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:40:14 2023

@author: ranaweer
"""
import numpy as np

N = 1000

# Using a Loop
hits = 0;
for i in range(N):
    x = np.random.random()
    y = np.random.random()
    r = np.sqrt(x**2 + y**2)
    
    if r < 1:
        hits = hits + 1

pi_estimate_1 = hits / N * 4
print("pi_estimate_1 =", pi_estimate_1)



# Using Array Maths
# =================

x = np.random.random((2,N))
r = np.sqrt(x[0,:]**2 + x[1,:]**2)

hitsB = len(r[r<1])

pi_estimate_2 = hitsB / N * 4

print("pi_estimate_2 =", pi_estimate_2)