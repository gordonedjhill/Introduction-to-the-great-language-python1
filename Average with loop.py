#CSI 31 GORDON EDJHILL
#AVERAVE OF NUMBER.py


numbers = input("How many numbers you want to calculate? ")
the_list = []

def calculate():
    for i in range (numbers):
        averages = float(input("Please enter the numbers you would like to find the averages of: "))
        the_list.append(averages)
    average = sum(the_list)/numbers
    print 'the average of the numbers are: ' , str(average)
    
calculate()


"""
How many numbers you want to calculate? 3
Please enter the numbers you would like to find the averages of: 54
Please enter the numbers you would like to find the averages of: 65
Please enter the numbers you would like to find the averages of: 70
the average of the numbers are:  63.0
