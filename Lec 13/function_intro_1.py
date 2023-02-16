## Computes the volumne of a cube
# @param sideLength: the length of a side
# @return the volume of the cube
#
def cubeVolume(sideLength):
    volume = sideLength ** 3
    return volume


side = 5;
vol = cubeVolume(side)
print(f"Volume of a cube with side {side} is {vol}")

