from  swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(turtle,length):
    for i in range(4):
        fd(turtle, length)
        lt(turtle)

square(bob,60)

def polygon(turtle,length,angle):
    sides = 360 / angle;
    for i in range(sides):
        fd(turtle, length)
        lt(turtle,angle)

polygon(bob,100,60)

wait_for_user()