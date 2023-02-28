## Computes the volumne of a cube
# @param sideLength: the length of a side
# @return 
#    The volume of the cube if sideLength is positive, 
#    or zero, otherwise
#
def cubeVolume2(sideLength):
    if sideLength < 0:
        return 0 #Returns the function immediately
    
    volume = sideLength ** 3
    return volume



## Computes the volumne of a cube
# @param sideLength: the length of a side
# @return 
#    The volume of the cube if sideLength is positive, 
#    or None, otherwise
#
def cubeVolume3(sideLength):
    if sideLength >= 0:        
        volume = sideLength ** 3
        return volume
    

# Testing
print("cubeVolume2(5) =", cubeVolume2(5))
print("cubeVolume2(-2) =", cubeVolume2(-2))

print("cubeVolume3(5) =", cubeVolume3(5))
print("cubeVolume3(-2) =", cubeVolume3(-2))

