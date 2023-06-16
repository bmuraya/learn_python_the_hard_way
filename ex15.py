# import sys and specify argv module
from sys import argv

#define varariable to the argv function 
script, filename = argv

# txt var assign to open external file 
txt = open(filename)

#print name of the external file and reads content in the file 
print(f"Here's your file {filename}:")
print(txt.read())

txt.close()

#request to input  name file
#print("Type the filename again:")
#file_again = input("> ")

#open file name
#txt_again = open(file_again)
#read content in the file 
#print(txt_again.read())
