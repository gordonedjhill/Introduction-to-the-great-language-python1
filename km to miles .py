#converts km to miles
#kmtomi.py

def main():
    print("This program prints the convertion of Kilometeers(KM) to Miles(M).")
    print('--------------------------------------------------------------')

    km = eval(input('Please enter the kilometers you would like to convert to miles: '))


    m = km / 1.61



    print("the conversion of", km ,"km to miles is :", ((format(m , ".2f"))))

main()



"""

This program prints the convertion of Kilometeers(KM) to Miles(M).
--------------------------------------------------------------
Please enter the kilometers you would like to convert to miles: 23
the conversion of 23 km to miles is : 14.29
