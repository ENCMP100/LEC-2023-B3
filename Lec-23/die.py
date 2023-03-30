##
#  This module defines a class that models a 6-sided die.
#
from random import randint
from matplotlib.patches import Rectangle, Circle

## A simulated 6-sided die that can be rolled and drawn on a canvas.
#
class Die:
    ## Constructs the die.
    #  @param x the upper-left x-coordinate of the die
    #  @param y the upper-left y-coordinate of the die
    #  @param size the size of the die
    #
    def __init__(self, x, y, size=60):
        self._x = x
        self._y = y
        self._size = size
        self._value = 1
        self._fillColor = 'white'
        self._outlineColor = 'black'
        self._dotColor = 'black'

    ## Get the face value of the die.
    #  @return the face value
    #
    def faceValue(self):
        return self._value

    ## Get the upper-left x-coordinate of the die.
    #  @return the x-coordinate
    #
    def getX(self):
        return self._x

    ## Get the upper-left y-coordinate of the die.
    #  @return the y-coordinate
    #
    def getY(self):
        return self._y

    ## Get the size of the die.
    #  @return the die size
    #
    def getSize(self):
        return self._size

    ## Set the fill and outline colors of the die face.
    #  @param fill the fill color
    #  @param outline the outline color
    #
    def setFaceColor(self, fill, outline):
        self._fillColor = fill
        self._outlineColor = outline

    ## Set the color used to draw the dots on the die face.
    #  @param color the dot color
    #
    def setDotColor(self, color):
        self._dotColor = color

    ## Simulates the rolling of the die using the random number generator.
    #
    def roll(self):
        self._value = randint(1, 6)

    ## Draws the die on the canvas.
    #  @param ax the graphical canvas on which to draw the die
    #
    def draw(self, ax):
        # The size of the dot and positioning will be based on the
        # size of the die.
        dotSize = self._size/10
        offset1 = dotSize*2
        offset2 = dotSize*5
        offset3 = dotSize*8
        # Draw the rectangle for the die.
        fill = self._fillColor
        outline = self._outlineColor
        ax.add_patch(Rectangle([self._x, self._y], self._size, self._size,
                               facecolor=fill, edgecolor=outline, linewidth=2))
        # Set the color used for the dots.
        color = self._dotColor
        # Draw the center dot or middle row of dots, if needed.
        if self._value == 1 or self._value == 3 or self._value == 5:
            ax.add_patch(Circle([self._x + offset2, self._y + offset2], dotSize,
                                facecolor=color, edgecolor=color, linewidth=1))
        elif self._value == 6:
            ax.add_patch(Circle([self._x + offset1, self._y + offset2], dotSize,
                                facecolor=color, edgecolor=color, linewidth=1))
            ax.add_patch(Circle([self._x + offset3, self._y + offset2], dotSize,
                                facecolor=color, edgecolor=color, linewidth=1))
        # Draw the upper-left and lower-right dots, if needed.
        if self._value >= 2:
            ax.add_patch(Circle([self._x + offset1, self._y + offset1], dotSize,
                                facecolor=color, edgecolor=color, linewidth=1))
            ax.add_patch(Circle([self._x + offset3, self._y + offset3], dotSize,
                                facecolor=color, edgecolor=color, linewidth=1))
        # Draw the lower-left and upper-right dots, if needed.
        if self._value >= 4:
            ax.add_patch(Circle([self._x + offset1, self._y + offset3], dotSize,
                                facecolor=color, edgecolor=color, linewidth=1))
            ax.add_patch(Circle([self._x + offset3, self._y + offset1], dotSize,
                                facecolor=color, edgecolor=color, linewidth=1))
