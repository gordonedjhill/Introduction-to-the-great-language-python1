#distance between two point.py
#gordon.edghill
import math
def main():
    
    print("this programs calculates the distance between two(2) points")
    print("------------------------------------------------------------")
    print("please enter your first set of points x and y respectively")
    x1 = eval(input("X :"))
    y1 = eval(input("Y :"))
    print("please enter your second set of points x and y respectively")
    x2 = eval(input("X :"))
    y2 = eval(input("Y :"))
    print (x1,y1,x2,y2)
    distance = math.sqrt((math.pow(x2 - x1,2)) + (math.pow(y2 - y1,2)))
    print("THE DISTANCE OF BETWEEN THE TWO POINTS IS : " , round(distance ,3))
main()    
