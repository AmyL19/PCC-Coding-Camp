# WHAT IS PYTHON?
Python is a general-purpose, versatile and popular programming language. It’s great as a first language because it is concise and easy to read, and it is also a good language to have in any programmer’s stack as it can be used for everything from web development to software development and scientific applications. Python also works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).


# HELLO WORLD
+ create a file: `first.py`
+ write some code in the file:
```{python}
print("hello world")
```
+ in the command line, run:
```
python first.py
```
+ the output should read: `'hello world'`

**Congrats! You've written your first program!**


# PYTHON COMMAND LINE
Type into the command line: `python`

From there you can write any python, including our hello world example from earlier in the tutorial:
```
	# C:\Users\Your Name>python
	# Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
	# Type "help", "copyright", "credits" or "license" for more information.
	>>> print("Hello, World!")
```

Whenever you are done in the python command line, you can simply type `exit()` to quit the python command line interface.

\pagebreak


# PYTHON VARIABLES

VARIABLES are containers for storing data values. In Python, there is no command for declaring a variable. Variables are created the moment you first assign a value to it.

```{python}
x = 5 							# x is the name of this variable, and 5 is the value that it holds
y = "hippo"						# assign value "hippo" to variable y
```


# VARIABLE NAMES

A few rules for Python variable names:
+ a variable must start with a letter or underscore (cannot start with a number)
+ a variable can only contain alpha-numeric characters and underscores
+ variable names are case-sensitive

## Legal variable names:
```{python}
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

## Illegal variable names:
```{python}
2myvar = "John"
my-var = "John"
my var = "John"
```


# VARIABLE TYPES

What differences do you notice between the variables `x` and `y`? Well, `x` is a variable that holds a number and `y` holds a word. This difference between the kind of values stored in a variable is called TYPES. Variables that store different kinds of values have different types. The type of a variable can be changed after the variable has been set.

```{python}
x = 4 							# x is of type int
x = "peachy" 					# now x is of type string
```

\pagebreak


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
# Here are a few examples:

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





