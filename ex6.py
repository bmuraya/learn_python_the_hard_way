types_of_people = 10  # define a variable  and assign it a value of 10 

# insert the variable into a new string which wwe assign to the variable x
x = f"There are {types_of_people} types of people." 


binary = "binary" # define a variable with the string  "binary"
do_not = "don't"   # define a variable with the string  "don't"

# insert the two string variable "binary"  and "don't" into a new string which we assign to the variable y
y = f"Those who know {binary} and those who {do_not}."

#we print  value for variable x and y  
print(x) #print 
print(y) #print 

#we print a string with value for variable x and y  using f-string format 
print(f"I said: {x}")  
print(f"I also said: '{y}'") 

# assign a boolean value to a variable
hilarious = False

#define a new string variable with placeholder {}
joke_evaluation = "Isn't that joke so funny?! {}"

#print out the value of joke_evaluation var using format()  add var hilarious into it
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

#print value of variable  w and E and concatenating the variables 
print(w + e) #print 