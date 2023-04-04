# Gorillas main program

from GorillasGame import GorillasGame
import time

game = GorillasGame()
game.setStage()
iterationCount = 1

while game.shouldPlay():
    
    if iterationCount % 10 == 0:
        game.setStage()
        
    game.positionPlayers()   
    game.showStage()
    game.shoot()
    game.showPlot()
    
    time.sleep(1)
    
    game.changeActivePlayer()
    
    iterationCount = iterationCount + 1
 
    

