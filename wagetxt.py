#Gordonedjhill
#Wages calculation

def payroll(sal):
    k=0
    payroll = 0
    while k <= 9:
        payroll = payroll + sal
        k = k + 1
    return payroll

def main():
    file = "namesWages.txt"
    file2 = "payroll.txt"
    outfile = open(file2, 'w')    
    with open(file, 'r') as f:
        for line in f:
            first = line.split()
            uname = (first[1])
            uname2 =  (first[0])
            print()
            wage = (first[2])
            wage = eval(wage)
            hour = (first[3])
            hour = eval(hour)
            sal = hour * wage
            payrol = payroll(sal)
            print(uname,"",uname2,"$",sal, file = outfile)
            
            
           
    print ("The payroll for the week is $",payrol,file = outfile)
      
main()    
