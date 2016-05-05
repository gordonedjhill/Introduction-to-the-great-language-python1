#gordon
#Word ,liines and character count.py

def main():
  print("This programs print the amount of Words , lines and Character in a a file.")
  print()
  fname = "inputs.txt"
  lines = 0
  words = 0
  chars = 0

  with open(fname, 'r') as f:
    for line in f:
        infile = line.split()

        lines += 1
        words += len(infile)
        chars += len(line)
  print("The number of words in the documents are :", words)
  print("The number of lines in the documents are :", lines)
  print("The number of character in the documents are :", chars)
main()        


"""
This programs print the amount of Words , lines and Character in a a file.

The number of words in the documents are : 78
The number of lines in the documents are : 4
The number of character in the documents are : 429
