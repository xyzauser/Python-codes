# This code was written by xyza.user !!!!

print("AUTHOR: xyza.user")

import math
from turtle import *

# Heart parametric equations
def hearta(t):
    return 15 * math.sin(t) ** 3

def heartb(t):
    return 12 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

speed(0)
bgcolor("black")
color("red")
penup()


# heart 1
for i in range(0, 360):
    t = math.radians(i)   # convert degree to radian
    x = hearta(t) * 5   #adjust the size
    y = heartb(t) * 5   #adjust the size
    goto(x, y)
    pendown()

# If you want to add multiple layers in heart then you can remove the comment ("""") from in the following lines 

"""
heart 2
for i in range(0, 360):
    t = math.radians(i)   
    x = hearta(t) * 10      #size of heart
    y = heartb(t) * 10
    goto(x, y)
    pendown()
"""

"""
#heart 3
for i in range(0, 360):
    t = math.radians(i)   
    x = hearta(t) * 20
    y = heartb(t) * 20
    goto(x, y)
    pendown()
"""
done()
