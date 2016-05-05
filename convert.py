# convert.py
#     A program to convert Celsius temps to Fahrenheit


def main():
    print("this program prints the convertion from Celsius to Fahrenheit")
    print('--------------------------------------------------------------')


    i = 1
    while i <= 5:
        celsius = input("What is the Celsius temperature? ")
        fahrenheit = 9.0/5.0 * celsius + 32
        i = i + 1
        print 'The temperature is :', fahrenheit, 'degrees Fahrenheit.'

main()


""""
this program prints the convertion from Celsius to Fahrenheit
--------------------------------------------------------------
What is the Celsius temperature? 0
The temperature is : 32.0 degrees Fahrenheit.
What is the Celsius temperature? 10
The temperature is : 50.0 degrees Fahrenheit.
What is the Celsius temperature? 20
The temperature is : 68.0 degrees Fahrenheit.
What is the Celsius temperature? 30
The temperature is : 86.0 degrees Fahrenheit.
What is the Celsius temperature? 40
The temperature is : 104.0 degrees Fahrenheit.
