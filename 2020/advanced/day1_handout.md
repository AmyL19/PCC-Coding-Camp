# ============= PYTHON VARIABLES =============

# VARIABLES are containers for storing data values.
# In Python, there is no command for declaring a variable. Variables are created the moment you
# first assign a value to it.

x = 5 # x is the name of this variable, and 5 is the value that it holds
y = "hippo"
print(x)
print(y)



# ============= VARIABLE NAMES =============

# a few rules for Python variable names:
# - a variable must start with a letter or underscore (cannot start with a number)
# - a variable can only contain alpha-numeric characters and underscores
# - variable names are case-sensitive

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"



# ============= VARIABLE TYPES =============

# What differences do you notice between the variables x and y? 
# Well, x is a variable that holds a number and y holds a word
# This difference between the kind of values stored in a variable is called TYPES
# Variables that store different kinds of values have different types.
# The type of a variable can be changed after the variable has been set.

x = 4 # x is of type int
x = "peachy" # now x is of type string



# ============= DISPLAYING VARIABLES =============

# One way to output the value of a variable is to use a PRINT statement
# print() is a builtin Python function that 
	# -> takes in a variable or value and
	# <- prints it out to the console

print("Hello World")
x = "Hello World"
print(x)



# ============= PYTHON STRINGS =============

# STRINGS in python are a sequence of characters surrounded by single or double quotation marks
# Here are a few examples of strings
x = "hello"
y = ""
z = "hello! 123abc?"
print(z)

# Strings can span multiple lines by using triple quotes
lonngggg_string = """Lorem ipsum dolor sit amet,
	consectetur adipiscing elit,
	sed do eiusmod tempor incididunt
	ut labore et dolore magna aliqua."""
print(lonngggg_string)

# To get the length of a string, you can use the len() function
a = "Hello, World!"
print(len(a))



# ============= STRING CONCATENATION =============
# To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

# You can only concatenate a string with another string
age = 36
txt = "My name is John, I am " + age
print(txt)



# ============= STRING INTERPOLATION =============
# using the 'f' prefix, you can embed expressions inside of strings

name = 'World'
program = 'Python'
print(f'Hello {name}! This is {program}')

a = 12
b = 3
print(f'12 multiply 3 is {a * b}.')



# ============= STRING INPUTS ==============
# input(s) prints out a prompt s (where s is a string) and returns the user's response
x = input('Enter your name:') 
print('Hello, ' + x)



# ============= STRING METHODS =============
# Python has a set of built-in methods that you can use on strings.
# Here are a few examples.

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']





