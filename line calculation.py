#gradient of line.py
#gordonedghill

def main():
    print("This programs calculates the slope of a line through non-vertical points. ")

    print("Please enter the first cordinates of the line")
    x1 = eval(input("X 1 = "))
    y1 = eval(input("Y 1 = "))
    

    print("please enter the second cordinates of the line")
    x2 = eval(input("X 2 = "))
    y2 = eval(input("Y 2 = "))
    




    m1 = x2 -x1
    m2 = y2 - y1
   

    if (m2 == 0):
        print ("Please revise your Y cordinates they would equate to 0. ")
        print ("please enter your y coridnates again -_-")
        y1 = eval(input("Y 1 = "))
        y2 = eval(input("Y 2 = "))
        m2 = y2 - y1
        m3 = m1 / m2
        print("The gradient of the line with cordinates A(",x1,y1,") & B(",x2,y2,") is :",round(m3,3))
        print("--------------------------------------------------------------------------------")
        print ("The equation of line in form of y = mx + c is :")
        y = y2 - y1
        x = x2 - x1
        m = m3 * x
        print ("y =" ,round(m,3),"+",y)
    else:
        m4 = m1 / m2
        print("The gradient of the line with cordinates A(",x1,y1,") & B(",x2,y2,") is :",round(m4,3))
        print("--------------------------------------------------------------------------------")
        print ("The equation of line in form of y = mx + c is :")
        y = y2 - y1
        x = x2 - x1
        m = m4 * x
        print ("y =" ,m,"+",y)
        
    
main()

"""
NB : testing with invalid Y's


This programs calculates the slope of a line through non-vertical points. 
Please enter the first cordinates of the line
X 1 = 23
Y 1 = 25
please enter the second cordinates of the line
X 2 = 34
Y 2 = 25
Please revise your Y cordinates they would equate to 0. 
please enter your y coridnates again -_-
Y 1 = 25
Y 2 = 45
The gradient of the line with cordinates A( 23 25 ) & B( 34 45 ) is : 0.55
--------------------------------------------------------------------------------
The equation of line in form of y = mx + c is :
y = 6.05 + 20



