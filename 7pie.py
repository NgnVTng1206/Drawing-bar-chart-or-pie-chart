from SimpleGraphics import *

#Author:  James Tam
#Version: July 27, 2026


"""
Learning: using diffent parameters to produce different effects for the pies.
"""
#To leverage your previous learning the same parameters used to draw the arcs will also
#be used to draw the 'pies'
setWidth(5)
setOutline("red")
pieSlice(100, 450, 100, 100, 0, 45)
setOutline("blue")
pieSlice(100, 450, 100, 100, 90, 45)
setOutline("green")
pieSlice(100, 450, 100, 100, 180, 45)
setOutline("yellow")
pieSlice(100, 450, 100, 100, 300, 45)

input("Press enter to see the big slice")
setWidth(15)
setOutline("grey")
pieSlice(100, 450, 100, 100, 270, 330)


