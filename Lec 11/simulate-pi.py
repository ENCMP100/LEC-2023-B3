#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:40:14 2023

@author: ranaweer
"""
import numpy as np

N = 10000000

# Using a Loop
hits_inside_circle = 0;
for i in range(N):
    x = np.random.random()
    y = np.random.random()
    dist_of_point_from_centre = np.sqrt((x-0.5)**2 + (y-0.5)**2)
   
    if dist_of_point_from_centre < 0.5:
        hits_inside_circle = hits_inside_circle + 1

pi_estimate_1 = hits_inside_circle / N * 4
print("pi_estimate_1 =", pi_estimate_1)

]

# Using Array Maths
# =================

x = np.random.random((N,1))
y = np.random.random((N,1))

dist_of_point_from_centre = np.sqrt((x-0.5)**2 + (y-0.5)**2)
index = dist_of_point_from_centre < 0.5

hitsB = len(dist_of_point_from_centre[index])

pi_estimate_2 = hitsB / N * 4

print("pi_estimate_2 =", pi_estimate_2)