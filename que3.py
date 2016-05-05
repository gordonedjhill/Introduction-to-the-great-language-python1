 #Gordon_edjhill
#Hourly pay

def intro():
    print(" This programs calculate the hourly rate and calculate")
    print("the total wages for the week. ")
    
def salary(n,hours,rate):
    i = 0
    while i <= n :
         n = i + 1
         return rate * hours
       
        

def payroll(n,sal):
    k=1
    payroll = 0
    while k <= n:
        payroll = payroll + sal
        k = k + 1
    return payroll
    
def main():
    intro()
    print()
    n = eval(input("How many employees salary would you like to calaculate"))
    rate = eval(input("Please enter the rate of which you are payed: "))

    i = 1
    while i <= n :
        hours = eval(input("Please enter the amount of hours you worked for the week: "))
        pay = salary(n,hours,rate)
        roll = payroll(n,pay)
        i = i + 1
        print("-------------------------------------------------")
        print ("Your salary for the week is :",pay)
      
    print()
    print( "The total payroll for the week is",roll) 
   
main()    

"""
This programs calculate the hourly rate and calculate
the total wages for the week. 

How many employees salary would you like to calaculate3
Please enter the rate of which you are payed: 15
Please enter the amount of hours you worked for the week: 50
-------------------------------------------------
Your salary for the week is : 750
Please enter the amount of hours you worked for the week: 50
-------------------------------------------------
Your salary for the week is : 750
Please enter the amount of hours you worked for the week: 50
-------------------------------------------------
Your salary for the week is : 750

The total payroll for the week is 2250
