"""
Created on Tue Jan 24 15:29:12 2023

@author: ranaweer
"""
import numpy as np
import matplotlib.pyplot as plt

N = 11
BW = 12
splatX = []
splatY = []

def main():
    (stageX, stageY) = createStage()
    
    winner = ''
    
    play = True
    while play:
        playerIndicies = getPlayerIndicies(stageX, stageY)
        trajectoryX = []
        trajectoryY = []
        
        showScene(stageX, stageY, playerIndicies, trajectoryX, trajectoryY)

        # Player 1 is playing
        (angle, velocity) = getThrowParameters(0)
        (trajectoryX, trajectoryY, splatBuildingIndex) = calcTrajectory(
            stageX, stageY, 0, playerIndicies[0], angle, velocity)

        showScene(stageX, stageY, playerIndicies, trajectoryX, trajectoryY)

        if splatBuildingIndex == playerIndicies[1]:
            winner = 'Player 1'
            break # breaks the while loop
        
        # Player 2 is playing
        (angle, velocity) = getThrowParameters(1)
        (trajectoryX, trajectoryY, splatBuildingIndex) = calcTrajectory(
            stageX, stageY, 0, playerIndicies[1], angle, velocity)
        
        showScene(stageX, stageY, playerIndicies, trajectoryX, trajectoryY)

        if splatBuildingIndex == playerIndicies[0]:
            winner = 'Player 2'
            break # breaks the while loop
            
        # Check if the user intends to play another round
        play_again = input('Enter Y to play another round:')
        if not (play_again == 'Y' or play_again == 'y'):
            play = False

    
    # Done playing
    if not winner == '':
        print(winner, 'Won! Game Over ...')
    
    print('Thank you for playing.')
    
    
    
def createStage():   
    stageX = np.arange(0, N) * BW #Positions (m).
    stageY = (1 + np.random.random(stageX.shape) * N) * N/2
    return (stageX, stageY)

def getPlayerIndicies(stageX, stageY):
    # First player on a building in the first half of the stage and the second
    # player on the second half of the stage. Skip the first and last buildings
    index1 = np.random.randint(1, N//2)
    index2 = np.random.randint(N//2, N-302)
    return (index1, index2)  
    
def showScene(stageX, stageY, playerIndicies, trajectoryX, trajectoryY):
    
    N = len(stageX)
    
    #Plotting the stage and the players
    plt.bar(stageX, stageY, width=BW*0.9)
    plt.axis([0, max(stageX), 0, np.round(N**2)])
    plt.plot(stageX[playerIndicies[0]], stageY[playerIndicies[0]]+4, '*r', markersize=15)
    plt.plot(stageX[playerIndicies[1]], stageY[playerIndicies[1]]+4, '*r', markersize=15)
   
    # Plotting the trajectory of the banana
    if len(trajectoryY) > 0:
        plt.plot(trajectoryX, trajectoryY, 'r')
    
    if len(splatX) > 0:
        plt.plot(splatX, splatY, "*r")
    
    plt.show()
 
def getThrowParameters(playerNumber):
    if playerNumber == 0: # giving first turn to the first player
        print("Player 1 (facing east)")
        angle = float(input("    Angle (degrees): "))
    else: # giving the second turn to the second player
        print("Player 2 (facing west)")
        angle = 180 - float(input("    Angle (degrees): "))    
    
    angle = np.radians(angle)
    velocity = float(input("    Velocity (m/s): ")) 
    
    return (angle, velocity)

def calcTrajectory(stageX, stageY, playerNumber, playerIndex, a, v):
    
    global splatX
    global splatY
    
    t = np.arange(0, 1000, 0.1) # time (s)
    g = 9.81
    
    x = v *  np.cos(a) * t
    y = v * np.sin(a) * t - 0.5 * g * t**2
    
    x = stageX[playerIndex] + x
    y = stageY[playerIndex] + y
    
    
    #Stop the banana when it splats on a building
    #
    # calculate the closest building index for every
    # x value
    buildingIndex = -1
    splatBuildingIndex = -1
    for i in range(1, len(x)):
        
        # We want to limit the trajectoty within the
        # range of x values in stageX
        if x[i] < stageX[0] or x[i] > stageX[N-1]:
            break
        
        buildingIndex = int(np.round(x[i]/BW))
        if y[i] < stageY[buildingIndex]:
            # Hits the building
            np.append(splatX, x[i])
            np.append(splatY, y[i])
            splatBuildingIndex = i
            break # breaks the for loop
            
    # we do not need any trajectory beyond the 
    # the current ''th posiiton
    x = x[0:i+1]
    y = y[0:i+1]
    
    return (x, y, splatBuildingIndex)
    
 
main()
