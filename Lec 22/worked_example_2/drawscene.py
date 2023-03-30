##
#  Draws simple figures on the canvas based on data in a text file.
#

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse

def main():
    infile = open('lamppost.fig', 'r')
    ax = configureWindow(infile)
    objData = extractNextLine(infile)
    while objData != "":
        drawObject(objData, ax)
        objData = extractNextLine(infile)
    infile.close()
    plt.show()

## Configures the graphics window based on the canvas parameters from
#  the scene file.
#  @param infile the text file containing the scene description
#  @return the canvas used for drawing
#
def configureWindow(infile):
    # Extract the window size.
    width = int(extractNextLine(infile))
    height = int(extractNextLine(infile))
    # Extract the background color.
    color = extractNextLine(infile)
    color = color.strip()
    # Create the window and set the background color.
    plt.axis([0, width-1, 0, height-1])
    ax = plt.gca()
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_aspect('equal', 'box')
    ax.set_facecolor(color)
    # Return the canvas object.
    return ax

## Extracts a single non-comment line from the text file.
#  @param infile the text file containing the scene description
#  @return the next non-comment line as a string or the empty string if the
#  end of file was reached
#
def extractNextLine(infile):
    line = infile.readline()
    while line != "" and line[0] == "#":
        line = infile.readline()
    return line

## Draws a single object on the canvas based on the description extracted
#  from a scene file.
#  @param objData a string containing the description of an object
#  @param ax the canvas on which to draw
#
def drawObject(objData, ax):
    # Extract the object data. All objects share the first 4 fields.
    parts = objData.split(",", 4) # Split into 5 parts.
    objType = parts[0].strip()
    x = int(parts[1])
    y = int(parts[2])
    outline = parts[3].strip()
    params = parts[4].strip()
    # Set the object color. All objects have an outline color.
    if outline == "dark green":
        outline = (0, 100/255, 0)
    # The last substring from the split contains the parameters for the
    # given object, which depends on the type of the object.
    if objType == "text":
        ax.text(x, y, params, color=outline, verticalalignment='top')
    else:
        values = params.split(",")
        if objType == "line":
            endX = int(values[0])
            endY = int(values[1])
            ax.plot([x, endX], [y, endY], color=outline)
        else:
            # Extract the fill color and set the canvas to use it.
            fill = values[0].strip()
            if fill == "dark green":
                fill = (0, 100/255, 0)
            # Extract the width and height and use them to draw the object.
            width = int(values[1])
            height = int(values[2])
            if objType == "rect":
                ax.add_patch(Rectangle([x, y], width, height,
                                       edgecolor=outline, facecolor=fill))
            elif objType == "oval":
                ax.add_patch(Ellipse([x + width/2, y + height/2], width, height,
                                     edgecolor=outline, facecolor=fill))

# Start the program.
main()
