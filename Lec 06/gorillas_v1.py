"""
Created on Tue Jan 24 15:29:12 2023

@author: ranaweer
"""
import numpy as np
import matplotlib.pyplot as plt

# SETTING UP THE STAGE
maxNumFloors = 10
numBuildings = 10
floorHeight = 4 # m
buildingSeparation = 10 # m
stageX = np.arange(0, numBuildings*buildingSeparation, buildingSeparation)
stageY = floorHeight * (1 + np.trunc(np.random.random(stageX.shape) * maxNumFloors))

plt.bar(stageX, stageY, width=buildingSeparation*0.9)
plt.axis([0, max(stageX), 0, 2*maxNumFloors*floorHeight])

# PLACING 2 PLAYERS
# for now, place two players on the second and the second-last building
# TODO: place the players on random building indices where the
# player should be placed in the left (west) half of the stage and
# the second player should be in the right (east) half of the stage.
# Don't put the both players on the same building. 
index = [1, numBuildings-2]
plt.plot(stageX[index], stageY[index]+3, '*r', markersize=20)


# Player 1 throwing a banana
player1X = stageX[index[0]]
player1Y = stageY[index[0]]
a1 = float(input("Enter the angle for the player facing east: "))
v1 = float(input("Enter the velocity for the player facing east: "))
g = 9.81

a1Radians = np.radians(a1)
t = np.arange(0, 2, 0.1)
x = v1 *  np.cos(a1Radians) * t
y= v1 * np.sin(a1Radians) * t - 0.5 * g * t**2

# shift the origin of the projectile to the first player's coordinates 
plt.plot(player1X+x, player1Y+y+3, 'r')

# TODO: check the plot of the projectile as the angle
# of through doesn't seem right for angle=30, velocity=50

plt.axis([0, max(stageX), 0, 2*maxNumFloors*floorHeight])

plt.show()

# Player 2 throwing a banana
player2X = stageX[index[1]]
player2Y = stageY[index[1]]
a2 = 180 - float(input("Enter the angle for the player facing west: "))
v2 = float(input("Enter the velocity for the player facing west: "))

a2Radians = np.radians(a2)
x = v2 *  np.cos(a2Radians) * t
yv= v2 * np.sin(a2Radians) * t - 0.5 * g * t**2

plt.plot(stageX[index], stageY[index]+8, '*r', markersize=20)


# shift the origin of the projectile to the first player's coordinates 
plt.plot(player2X+x, player2Y+y+8, 'r')

# TODO: check the plot of the projectile as the angle
# of through doesn't seem right for angle=30, velocity=50

plt.show()





