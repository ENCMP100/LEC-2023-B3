#CLASS Stage
# Represents the stage of the gorillas game
#

import numpy as np
import matplotlib.pyplot as plt

class GorillasGame:
    USER_VS_KONG = 1
    KONG_VS_USER = 2
    USER_VS_USER = 3
    KONG_VS_KONG = 4
    
    # Constructor
    def __init__(self):
        self._N = 11
        self._BW = 5
        self.setStage()        
        self._activePlayer = 0
        self._playMode = GorillasGame.KONG_VS_KONG
        self._splatX = []
        self._splatY = []
        self._splatBuildingIndex = -1
    
    ## CREATE STAGE: creates the x and y coordinates of the 
    # stage that represents buildings  
    def setStage(self):
        self._stageX = np.arange(0, self._N) * self._BW #Positions (m).
        self._stageY = np.random.randint(3, 12, self._N)
        
    ## Displays the stage and the players
    def showStage(self):
        plt.bar(self._stageX, self._stageY, width=self._BW * 0.8)
        plt.axis([-self._BW/2, max(self._stageX) + self._BW/2, 0, 24])
        plt.plot(self._p1[0], self._p1[1], '*', color='purple')
        plt.plot(self._p2[0], self._p2[1], '*', color='green')
        ax = plt.gca()
        ax.set_aspect(1)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
       
    ## Calculates and positions players
    def positionPlayers(self):
        index1 = np.random.randint(0, int(len(self._stageX)/2)-1)
        x1 = self._stageX[index1]
        y1 = self._stageY[index1] + 0.5
        self._p1 = (x1, y1)
        
        index2 = np.random.randint(int(len(self._stageX)/2)+1, len(self._stageX))
        x2 = self._stageX[index2]
        y2 = self._stageY[index2] + 0.5
        self._p2 = (x2, y2)
        
    ## Determines whetehr the game should continue
    # To be implemented
    def shouldPlay(self):
        return True
    
    ## Allows selecting play mode
    def selectPlayMode(self):
        playMode = 0
        while not GorillasGame.USER_VS_KONG <= playMode <= GorillasGame.KONG_VS_KONG:
            try:
                print(f"{GorillasGame.USER_VS_KONG}: User vs Kong")
                print(f"{GorillasGame.KONG_VS_USER}: Kong vs User")
                print(f"{GorillasGame.USER_VS_USER}: User vs User")
                print(f"{GorillasGame.KONG_VS_KONG}: Kong vs Kong")

                playMode = int(input("Play mode: "))
            except:
                pass
            
        self._playMode = playMode
    
    ## Calculates and displays a trajectory of a throw
    #  Only a partial implementation so far
    def shoot(self):
        (v,a) = self.getKongInputs()
        x0,y0 = self.getActivePlayerXY()
        
        # Calculating the total time it would take by an object
        # that is traveling at the horizontal velocity component 
        # to travel across the entire stage
        T = max(self._stageX) / np.abs(v * np.cos(a))
        dt = T/1000
        
        # Calculate a time vector
        t = np.arange(0, T, dt)
        x = x0 + v * np.cos(a) * t
        y = y0 + v * np.sin(a) * t - 0.5 * 9.81 * t ** 2
        
        x,y = self.stripOutOfBoundTrajectorySegments(x,y)
        
        plt.plot(x, y, 'r')
        
    # Concludes a plot so that it is displayed to the user    
    def showPlot(self):
        plt.show()
    
    ## Takes the x,y coordinates of the active player
    # @return (x,y) as a tuple
    def getActivePlayerXY(self):
        if self._activePlayer == 0:
            return self._p1
        else:
            return self._p2
    
    ## Changes the active player
    def changeActivePlayer(self):
        if self._activePlayer == 0:
            self._activePlayer = 1
        else:
            self._activePlayer = 0     

    ## Provides randomy generated velocity and angle for the active player
    #  No input is obtained from the user
    def getKongInputs(self):
        v = np.random.randint(5, 30)
        a = np.random.randint(5, 80)
        
        if self._activePlayer == 1:
            a = 180 - a
        
        a = np.deg2rad(a)
        return (v,a)

    ## Removes the parts of a trajectory that is out of bound.
    #  A trajectory portion is out-of-bound if it leaves outside
    #  of the stage or if it represents a part that comes after 
    #  hitting a building.
    def stripOutOfBoundTrajectorySegments(self, x,y):
        #Stop the banana when it splats on a building
        #
        # calculate the closest building index for every
        # x value
        buildingIndex = -1
        self._splatBuildingIndex = -1
        for i in range(1, len(x)):
            
            # We want to limit the trajectoty within the
            # range of x values in stageX
            if x[i] < self._stageX[0] or x[i] > self._stageX[self._N-1]:
                break
            
            buildingIndex = int(np.round(x[i]/self._BW))
            if y[i] < self._stageY[buildingIndex]:
                # Hits the building
                np.append(self._splatX, x[i])
                np.append(self._splatY, y[i])
                self._splatBuildingIndex = buildingIndex
                break # breaks the for loop
                
        # we do not need any trajectory beyond the 
        # the current ''th posiiton
        x = x[0:i+1]
        y = y[0:i+1]
        
        return (x,y)