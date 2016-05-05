#rectangle.py
from graphics import*


def Values(p1,p2,win):
    Length =abs(p2.getX() - p1.getX())
    Width =abs(p2.getY() - p1.getY())
    Area = Length * Width
    Perimeter = 2 *(Length + Width)
    return Area , perimeter



    
def main():
    win = GraphWin("rectangle",400,400)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    frame = Rectangle(p1,p2)
    frame.draw(win)
    Length =abs(p2.getX() - p1.getX())
    Width =abs(p2.getY() - p1.getY())
    Area = Length * Width
    perimeter = 2 *(Length + Width)
    print("Area is ", Area)
    print("Primeter is", perimeter)
main()    
