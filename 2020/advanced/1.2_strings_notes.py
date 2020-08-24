# ============= PYTHON STRINGS =============
# STRINGS in python are a sequence of characters surrounded by single or double quotation marks
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
# To CONCATENATE, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b # Merge variable a with variable b into variable c:
print(c)

# You can only concatenate a string with another string
age = 36
txt = "My name is John, I am " + age
print(txt)



# ============= STRING INTERPOLATION =============
# You can embed expressions inside of strings using the 'f' prefix
name = 'World'
program = 'Python'
print(f'Hello {name}! This is {program}')

a = 12
b = 3
print(f'12 multiply 3 is {a * b}.')



# ============= STRING INPUTS ==============
x = input('Enter your name:') # input(s) prints out a prompt s and returns the user's response
print('Hello, ' + x)



# ============= STRING METHODS =============
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


