# program that converts temperatures from Fahrenheit to Celsius.
# fahrenheit to celsius.py

def main():
    print("This program prints the convertion from Fahrenheit to Celsius.")
    print('--------------------------------------------------------------')




    far = eval(input('Please enter the Fahrenheit temperature you would like to convert to Celsius: '))


    celsius = (far  -  32)  *  5/9


    print("the conversion of", far ,"km to fahrenheit is :", ((format(celsius , ".3f"))))


  

main()


