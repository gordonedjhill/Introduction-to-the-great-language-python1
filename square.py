#Gordon Edjhill
#Sum of square

def intro():
    print("This program sums the square of numbers in a list")
    return

def toNumbers(strList):
    nums = []
    for n in strList:
        nums.append(eval(n))
    return nums

def squareEach(strList):
     nums = []
     for n in strList:
        nums.append(eval(n) **2)
     return nums
    
def sumList(squ):
    a = sum(squ)
    return a
    

def main():
    intro()
    filename = input("What is the name of the file ")
    infile = open(filename , 'r')
    lst = infile.readlines()
    print(lst)
    nums = toNumbers(lst)
    print(nums)
    squ = squareEach(lst)
    print("The squares",squ)
    su = sumList(squ)
    print("The sum of square",su)
main()    

"""
This program sums the square of numbers in a list
What is the name of the file num.txt
['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9']
[1, 2, 3, 4, 5, 6, 7, 8, 9]
The squares [1, 4, 9, 16, 25, 36, 49, 64, 81]
The sum of square 285
