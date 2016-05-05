#Newtwn law.py
#gordon.edjhill

def main():
    print("this programs calculates the Squareroot of a number ")
    num = eval(input("please enter the number you would like to find the square root of please  clown enter it now "))
    i = 0
    guest = num / 2
    
        
    
    while( i < 10 ):
        i =  i + 1
        guest = (guest + (num/guest)) / 2
        guest2 = (guest + (num/guest)) /2
        print("the square root is" , (round  ( guest ,2)))
        print("The Difference between first guest is  ",(round(guest - guest2,2)))
   
   


       
        
    
main()    
