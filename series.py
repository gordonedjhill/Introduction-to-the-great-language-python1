#Gordon.py
#Syracuse


def intro():
    print("This programs print out the Syracuse sequence for any natural number ")


def syracuse_seq(u):
       
    seq = [u]

    while u > 1:

        if u % 2 == 0:
            u = u/2

        else:
            u = 3*u + 1

        seq.append(u)

    return seq

def main():
    intro()
    u = eval(input("please enter the natural number : "))
    sei = syracuse_seq(u)
    print(sei)
    
main()    

"""
This programs print out the Syracuse sequence for any natural number 
please enter the natural number : 6
[6, 3.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]
