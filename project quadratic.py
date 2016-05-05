#mid term
#quadratic solutons.py
#gordon_edjhill
import math
   

def intro():
    print("This program evaluates Quadratic equatons in the standard form")
    print("of ax^2 + bx + c and a, b and c are real numbers (R)")
    print("---------------------------------------------------------------")

def getinfo():
    a = eval(input("please enter the coefficient a :"))
    b = eval(input("please enter the coefficient b :"))
    c = eval(input("please enter the coefficient c :"))

    if (a == 0):
        print("please enter a next value for a")
        a = eval(input("Please renter a it cannot be = 0 :"))
        return a,b,c

    else:
        return a,b,c
        

def dis(a,b,c):
    if ((((b**2) - (4*(a*c)))) == 0):
        print ("there is one real root : ")
        return print( -b,"/",2*(a)," or ", -b / (2*(a)))
        
    if ((((b**2) - (4*(a*c)))) < 0):
        print("The roots are complex and they are :")
        print("Root_1 =  .",round( -b / (2*(a)),3) , "+" , round(abs(((((b**2) - (4*(a*c)))))/ (2*(a))),3) ,"i" )
        return print("Root_2 =  .",round( -b / (2*(a)),3) , "-" , round(abs(((((b**2) - (4*(a*c)))))/ (2*(a))),3) ,"i" )

    else:
         print("The roots are:")
         print("root_2: " ,((round( -(b) / (2*(a)),3)) - (round(math.sqrt(((((b**2) - (4*(a*c))))))/ (2*(a))))))
         print("root_1:  " ,((round( -(b) / (2*(a)),3)) + (round(math.sqrt(((((b**2) - (4*(a*c))))))/ (2*(a))))))
    

def main():
    intro()
    a,b,c = getinfo()
    roots = dis(a,b,c)
main()
