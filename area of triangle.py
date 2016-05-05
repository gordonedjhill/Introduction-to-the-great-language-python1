#area of tirangle .py
#gordon edghill
import math

def main():
    print ("This program evalutes the area of a triangle.")
    print ("-----------------------------------------------")
    
    a = eval(input("please enter side A of the triangle :"))
    b = eval(input("please enter side B of the triangle :"))
    c = eval(input("please enter side C of the triangle :"))

    while ((a + b) < c ):
        print ("The points enter does not form a triangle please re-enter the point")
        a = eval(input("please enter side A of the triangle :"))
        b = eval(input("please enter side B of the triangle :"))
        c = eval(input("please enter side C of the triangle :"))
   
    s = float(a + b + c) / 2
    area = s - a
    area2 = s - b
    area3 = s - c
    area4 = area * area2 * area3
    area5 = s * area4
    area6 = math.sqrt(area5)
    


    print ("The area of the triangle with side : ","A =", a,",B =" ,b,", C =",c ,"is :", round(area6,4))
   
        
        
        
main()

"""
(with wrong points)

This program evalutes the area of a triangle.
-----------------------------------------------
please enter side A of the triangle :5
please enter side B of the triangle :5
please enter side C of the triangle :12
The points enter does not form a triangle please re-enter the point
please enter side A of the triangle :5
please enter side B of the triangle :5
please enter side C of the triangle :6
The area of the triangle with side :  A = 5 ,B = 5 , C = 6 is : 12.0


