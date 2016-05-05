# line info.py
from graphics import*
import math

def main():
    print("This programs calculates the slope and length of a given line")
    win = GraphWin("line_info",400,400)
    a = win.getMouse()
    b = win.getMouse()
    c = Line(a,b)
    c.draw(win)
    f = Line.getCenter(c)
    f.setFill("cyan")
    f.draw(win)
    dx = ((b.getX()) - (a.getX()))
    dy = ((b.getY()) - (a.getY()))

    if (dy == 0):
        print ("There is no slope")
    else:
        slope = round (dx/dy,2)
        length = round(math.sqrt(((dx**2) + (dy**2))),2)
        output = Text(Point(150,75),"")
        output.draw(win)
        output2 = Text(Point(200,40),"")
        output2.draw(win)

        Text(Point(100,75), "Slope :").draw(win)
        Text(Point(100,40), "Length of line :").draw(win)
        output.setText(slope)
        output2.setText(length)
    


    
main()    
