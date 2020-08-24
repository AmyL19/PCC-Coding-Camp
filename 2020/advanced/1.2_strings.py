# =============================== PYTHON STRINGS ==============================

x = "hello"
y = ""
z = "hello! 123abc?"
print(z)							

lonngggg_string = """Lorem ipsum dolor sit amet,
	consectetur adipiscing elit,
	sed do eiusmod tempor incididunt
	ut labore et dolore magna aliqua."""		# multi-line string
print(lonngggg_string)

a = "Hello, World!"
print(len(a))


# ============================ STRING CONCATENATION ===========================

a = "Hello"
b = "World"
c = a + b 			# Concatenate variable a with variable b into variable c:
print(c)

age = 36
txt = "My name is John, I am " + age		# this will fail
print(txt)


# ============================ STRING INTERPOLATION ===========================

name = 'World'
program = 'Python'
print(f'Hello {name}! This is {program}')	

a = 12
b = 3
print(f'12 multiply 3 is {True}.')


# =============================== STRING INPUTS ===============================

x = input('Enter your name:') # input(s) prints out a prompt s and returns the user's response
print('Hello, ' + x)


# =============================== STRING METHODS ==============================

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
