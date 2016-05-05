# convert.py
# A program to convert Celsius temps to Fahrenheit


def main():
    print("this program prints the convertion from Celsius to Fahrenheit")
    print('--------------------------------------------------------------')

    print('    CELSIUS      FAHRENHEIT')
    print('    ------------------------')


    i = 0
    while i <= 10:

        n = 0        
        celsius = (10 * i)
        fahrenheit = 9.0/5.0 * celsius + 32
        i = i + 1
       
      
        print( "{0:10.4f}{1:16.4f}" . format(celsius , fahrenheit))

main()


""""
this program prints the convertion from Celsius to Fahrenheit
--------------------------------------------------------------
    CELSIUS      FAHRENHEIT
    ------------------------
    0.0000         32.0000
   10.0000         50.0000
   20.0000         68.0000
   30.0000         86.0000
   40.0000        104.0000
   50.0000        122.0000
   60.0000        140.0000
   70.0000        158.0000
   80.0000        176.0000
   90.0000        194.0000
  100.0000        212.0000
