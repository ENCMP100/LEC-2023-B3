
"""
Created on Thu Feb  9 15:39:00 2023

@author: ranaweer
"""

"""
import numpy as np
import matplotlib.pyplot as plt

## ALLOCATE VARIABLES TO STORE DATA
time = np.arange(0, 24)
temp = np.zeros((24,))
windchill = np.zeros((24,))
windSpeed = np.zeros((24,))
"""

## READ DATA AND LOAD THEM INTO THE ALLOCATED VARIABLES
in_val = ""
next_block = ""
sentinel = "==="
while in_val != sentinel :
    in_val = input()
    
    if in_val == "Time (LST)":
        next_block = "time"
    elif in_val == "Temp (°C)":
        next_block = "temp"
    elif in_val == "Wind Spd (km/h)":
        next_block = "wind-speed"
    elif in_val == "Wind Chill (°C)":
        next_block = "wind-chill"
    elif in_val != sentinel:
        # Reading data
        print(next_block, ":", in_val)
    
print("Data input is complete")    





"""

## CREATE THE PLOTS OF TEMP AND WIND-CHILL VS TIME AND WIND SPEED VS TIME
plt.subplot(2, 1, 1)
plt.plot(time, temp, label='Temp')
plt.plot(time, windchill, label='Windchill')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, windSpeed, label='Wind Speed')
plt.legend()

"""

