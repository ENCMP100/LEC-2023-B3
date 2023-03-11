## Computes the volumne of a cube
# @param sideLength: the length of a side of the cube
# @return the volume of the cube
#
def cubeVolume(sideLength):
    volume = sideLength ** 3
    return volume
    

side = -5
volume = cubeVolume(side)
vol2 = cubeVolume(10)
print(f"Volume of a cube with side {side} is {volume}")
print("Volume of a cube with side", side, "is", volume)
print("Volume of a cube with side 10 is", vol2)





