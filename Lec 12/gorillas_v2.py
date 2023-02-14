"""
Created on Tue Jan 24 15:29:12 2023

@author: ranaweer
"""
import numpy as np
import matplotlib.pyplot as plt

# SETTING UP THE STAGE
N = 11 #Number of buildings
BW = 12 # Building Width
stageX = np.arange(0, N) * BW #Positions (m).
stageY = (1 + np.random.random(stageX.shape) * N) * N/2

#PLACING THE PLAYERS ON RANDOMLY SELECTED BUILDINGS
#First player on a building in the first half of the stage and
#the second player on the second half of the stage
index1 = int(np.trunc(np.random.random() * N//2))
index2 = N//2 + int(np.trunc(np.random.random() * N//2))

#Making sure we don't select the same building or adjuscent buildings
#for the two players
if index2 == index1 or index2 == index1+1:
    index2 = index1 + 2
elif index2 == N-1:
    index2 = N-2 # we don't want the player 2 on the last building either

#Plotting the stage and the players
plt.bar(stageX, stageY, width=BW*0.9)
plt.axis([0, max(stageX), 0, np.round(N**2)])
plt.plot(stageX[index1], stageY[index1]+4, '*r', markersize=15)
plt.plot(stageX[index2], stageY[index2]+4, '*r', markersize=15)
plt.show()
 
t = np.arange(0, 1000, 0.1) # time (s)
g = 9.81

#TODO 1: Repeat the play until a banana splats on the opponent's building
  
#Running two "throw cycles" alternated between the two players.
for playerNumber in range(2):
    
    if playerNumber == 0: # giving first turn to the first player
        print("Player 1 (facing east)")
        a = float(input("    Angle (degrees): "))
        activePlayerIndex = index1
    else: # giving the second turn to the second player
        print("Player 2 (facing west)")
        a = 180 - float(input("    Angle (degrees): "))
        activePlayerIndex = index2


    v = float(input("    Velocity (m/s): "))        
    a = np.radians(a)
    
    x = v *  np.cos(a) * t
    y = v * np.sin(a) * t - 0.5 * g * t**2
    
    x = stageX[activePlayerIndex] + x
    y = stageY[activePlayerIndex] + y
    
    #TODO 2: Stop the banana when it splat on a building
    
    # Ploting the full figure again since we already 
    # called plt.show() before
    #
    # Plotting the stage
    plt.bar(stageX, stageY, width=BW*0.9)
    plt.axis([0, max(stageX), 0, np.round(N**2)])
    
    # Plotting the players on the buildings
    plt.plot(stageX[index1], stageY[index1]+4, '*r', markersize=15)
    plt.plot(stageX[index2], stageY[index2]+4, '*r', markersize=15)
    
    # Plotting the trajectory of the banana
    plt.plot(x, y, 'r')
    plt.show()

    #TODO 3: End the game if the banana hit on the opponent's building


