#gordonedjhill.py
#Midterm (2)


#function to introduce the program
def intro():
    print ("This program tests the given userid and password against a file") 
    print ("of userids and passwords. ")
    
#gets infrmation
def getInfo():
    user = input("please enter your user ID: ") # userid info
    password = input("Please enter your password: ")  #password info
    return user, password

# fuction to do comparison
def checkFile(user , password):
    file = "unames_passwords.txt"  # assign the file name to file
    
    with open(file, 'r') as f: # opens file as f
        for line in f:         # Creates a loop through the file
            word = line.split() #seperates each word in the file
            if (user == word[0] and password == word[1]): #compare each word wih the given user ID and password
                return True
                break
        else:
            return False 
    f.close()
           
            
    
def main():
    intro()
    counter = 1  # keeps track of the amount of try 
    while counter <= 3 :  # runs the program to the exact number of attempt allowed
        userid,password = getInfo()  # grabs info from the function
        answer = checkFile(userid,password) #assign the answer and also in the brackets gives the value
        if answer == True: 
            print ("You have access to the worls largest database enjoy :)")
            break   # if the passsword is correct the program ends
        else:
            print ("You have ",counter,"failed attempt(maximim attempts are 3)") # if the answer is not correct it prints a statement 
            counter = counter + 1 # one is add to the counter if the id and password id not correct

    if answer == False : # if the 3 attempts is exceeded the closing line will be printed
        print("You have exceeded all of your attempts plese try again after 24 hourse bye :(")        
main()

"""
This program tests the given userid and password against a file
of userids and passwords. 
please enter your user ID: gordon
Please enter your password: Edghill
You have  1 failed attempt(maximim attempts are 3)
please enter your user ID: mad
Please enter your password: max
You have  2 failed attempt(maximim attempts are 3)
please enter your user ID: msmith
Please enter your password: boxer
You have access to the worls largest database enjoy :)
