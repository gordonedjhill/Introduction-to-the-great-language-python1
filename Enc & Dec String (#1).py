# GordonEdjhill 
# Cesar Ciper


def intro():
    print("This program will be able  encode and decode a string of text")
    return

def encode():
    Mes = input("Please enter the message you would like to encode?", )
    key = 5
    Enc = " "
    for ch in Mes:
        Enc = Enc + chr(ord(ch) + key)
    return Enc
        
        
def decode():
    Code = input("Please enter the Unicode you would like to decode." )
    Key = 5
    Dec = " "
    for ch in Code:
        Dec = Dec + chr(ord(ch) - Key)
    return Dec

def main():
    intro()
    choice = input("Would you Like to Encode or Decode a Message?(Please use E or D) ")
    if choice [0] == "E" :
        Enc = encode()
        print(Enc)
        
    elif choice [0] == "D" :
        Dec = decode()
        print(Dec)
    else :
        print("you have shamed your reading Professor.. Goodbye")

main()

"""
This program will be able  encode and decode a string of text
Would you Like to Encode or Decode a Message?(Please use E or D) E
Please enter the message you would like to encode?I am a boy
 N%fr%f%gt~
>>> main()
This program will be able  encode and decode a string of text
Would you Like to Encode or Decode a Message?(Please use E or D) D
Please enter the Unicode you would like to decode. N%fr%f%gt~
 I am a boy
