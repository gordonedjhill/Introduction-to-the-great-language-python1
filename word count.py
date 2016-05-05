#gordon.edjhill
#word count


  
def main():
  print("This program count the amount of words in a sentence")
  print()
  sen = input(str("please enter the sentenc your would like to count :"))
  print ("The sentence is :", sen)
  words = sen.split()
  count = len(words)
  print("The number of words in the sentence are:",count)
  
main()    

"""
This program count the amount of words in a sentence

please enter the sentenc your would like to count :The boy goes to Bronx College
The sentence is : The boy goes to Bronx College
The number of words in the sentence are: 6
