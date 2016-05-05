
from graphics import *
import math 
def main():
    print ("This programs computes the intersection")
    print ("of a circile and a horizontal line")
    r = eval(input("please enter a smaller radius of the circle: "))
    while r > 10 :
        r = eval(input("please enter the radius of the circle: "))
    y = eval(input("please enter the y intercept"))
    while y >= r or y <= 0:
        y = eval(input("please enter the y intercept"))

    win = GraphWin("circle line", 300, 300)
    win.setCoords(-10, -10, 10, 10)
    center = Point(0, 0)
    circ = Circle(center, r)
    circ.draw(win)
    circ.setFill("yellow")
    circ.setOutline("red")
    point1 = Point(10, y)
    point2 = Point(-10, y)
    line = Line(point1, point2)
    line.setFill("red")
    line.draw(win)

   # x1 = math.sqrt((math.pow(r,2) - (math.pow(y,2))))
    #print ("intersection point will be equall to  :",round(x1,3))

main()    


