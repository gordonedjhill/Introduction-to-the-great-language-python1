#program that converts meters to feet
#meters to feet.py

def main():
    print("This program prints the convertion of Meters(M) to Feet.")
    print('--------------------------------------------------------------')

    m = eval(input('Please enter the Meters(M) you would like to convert to Feet: '))


    ft = m * 3.2808



    print("the conversion of", m ,"Metrs to Feet is :", ((format(ft , ".2f"))))

main()


"""
This program prints the convertion of Meters(M) to Feet.
--------------------------------------------------------------
Please enter the Meters(M) you would like to convert to Feet: 20
the conversion of 20 Metrs to Feet is : 65.62
