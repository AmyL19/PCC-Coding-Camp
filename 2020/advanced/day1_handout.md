# PYTHON INTRO

## What is Python?
Python is a general-purpose, versatile and popular programming language. It’s great as a first language because it is concise and easy to read, and it is also a good language to have in any programmer’s stack as it can be used for everything from web development to software development and scientific applications. Python also works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).


## Hello World
+ create a file: `first.py`
+ write some code in the file:
```python
print("hello world")
```
+ in the command line, run:
```
python first.py
```
+ the output should read: `'hello world'`

**Congrats! You've written your first program!**


## Python command line
Type into the command line: `python`

From there you can write any python, including our hello world example from earlier in the tutorial:
```
	# C:\Users\Your Name>python
	# Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
	# Type "help", "copyright", "credits" or "license" for more information.
	>>> "Hello, World!")
```

Whenever you are done in the python command line, you can simply type `exit()` to quit the python command line interface.


## Python variables

VARIABLES are containers for storing data values. In Python, there is no command for declaring a variable. Variables are created the moment you first assign a value to it.

```python
x = 5 							# x is the name of this variable, and 5 is the value that it holds
y = "hippo"						# assign value "hippo" to variable y
```


## Variable names

A few rules for Python variable names:
+ a variable must start with a letter or underscore (cannot start with a number)
+ a variable can only contain alpha-numeric characters and underscores
+ variable names are case-sensitive

### Legal variable names:
```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

### Illegal variable names:
```python
2myvar = "John"
my-var = "John"
my var = "John"
```


## Variable types

What differences do you notice between the variables `x` and `y`? Well, `x` is a variable that holds a number and `y` holds a word. This difference between the kind of values stored in a variable is called TYPES. Variables that store different kinds of values have different types. The type of a variable can be changed after the variable has been set.

```python
x = 4 							# x is of type int
x = "peachy" 					# now x is of type string
```


## Displaying variables

One way to output the value of a variable is to use a PRINT statement; `print()` is a builtin Python function that takes in a variable or value and logs it to the console.

```python
print("Hello World")
x = "Hello World"
print(x)
```



# THE NUMERIC TYPE

## Basic examples

The `int` and `float` types are the ways that python can interact with numbers. `int` is short for integer, which refers to whole numbers, positive or negative. `float` refers to numbers that use decimals, like the following:

```python
type(5)							# class: int
isinstance(-3, int)				# True
type(0.5) 						# class: float
```


## Type conversions

Python makes converting between `float` and `int` very easy, using their namesake functions. When mixed, python will just automatically choose the most convenient type.

```python
x = 5
y = 4.0
z = 6.5

float(x) 						# 5.0
int(y)							# 4
int(z)							# 6 -- Note: just drops the decimal, not rounding
x + y							# what will this print? hint: implicit conversions
```

## Comparison

Python uses the same symbols to compare numbers as in math! The only difference is that when comparing for equality, python uses `==`, since `=` is used for variable assignment. The comparison operators that python understands are `<`, `>`, `<=`, `>=`, and `==`.

```python
5 == 5 							# True
5.0 == 5.0 						# True
5 == 4							# False
5 == 5.0						# True
5 < 6							# True
-1 > 0							# False
```


## Arithmetic

Python uses the `+`, `-`, `/`, and `*` operators as you would expect. Two operators that python understands that may be new to you are `//`, which is integer division (same as regular division, but rounds down and produces and `int`), and `%`, which is the modulo operator (the remainder after integer division). In evaluation, python follows the PEMDAS sequences (`%` is on the same level as division). Note that python also uses parentheses, if you need.

```python
5 + 3							# 8
9 - 6							# 3
3 * 21							# 63
10 / 3							# 3.33333
10 // 3							# 3
9 // 3							# 3
9 / 3							# 3.0
100 % 3							# 1
4 + 3 * 2						# Note: Remember PEMDAS!!
```


## Other built-in functions

Python has a bunch of useful functions for working with numbers -- all of these work with both the `int` and `float` types. Some examples include `abs`, `max`, `min`, `pow`, and `round`. 

```python
abs(-5)   						# absolute value
max(2, 3, 4, 5)  				# return the max value
min(2, 3)  						# return the min value
pow(2, 3)  						# raise to the given power (pow(x,y) == x**y)
round(2.354, 1) 				# round with the given number of digits
```

## Using the math library

Python has a lot more functions, stored in libraries that you can invoke as you need. One handy example is the `math` library, which holds a lot of mathematical functions that you can take advantage of. Some examples of usign the `math` library are shown below. A full list of the functions that the `math` library holds can be found at: https://docs.python.org/3/library/math.html.

```python
import math

math.sin(0)						# math.cos, math.tan, math.asin, etc.
math.floor(6.3)					# math.ceil exists also
math.sqrt(25)					# natural square root
math.log(math.e)				# default natural log, but can add base: math.log(4, 2) == 2
round(math.e, 3)				# e
round(math.pi, 3)				# pi
```



# THE STRING TYPE

## Intro to Strings

STRINGS in python are a sequence of characters surrounded by single or double quotation marks. Here are a few examples of strings: `"hello"`, `""`, and `"hello! 123abc?"`.

Strings can span multiple lines by using triple quotes:

```python
lonngggg_string = """Lorem ipsum dolor sit amet,
	consectetur adipiscing elit,
	sed do eiusmod tempor incididunt
	ut labore et dolore magna aliqua."""
```

To get the length of a string, you can use the len() function.

```python
a = "Hello, World!"
len(a)							# 13
```


## String Concatenation

To concatenate, or combine, two strings you can use the `+` operator.
For example, here is a merging of two variables, `a` and `b`: 

```python
a = "Hello "
b = "World"
a + b 							# "Hello World"
```

However, you can only concatenate a string with another string: 

```python
age = 36
txt = "My name is John, I am " + age  # this will fail
```


## String interpolation

Using the `f` prefix, you can embed expressions inside of strings. These expressions don't necessarily have to be strings:

```python
name = 'World'
program = 'Python'
f'Hello {name}! This is {program}'			# "Hello World! This is Python"

a = 12
b = 3
f'12 times 3 is {a * b}.'					# "12 times 3 is 36."
```


## String inputs

`input(s)` prints out a prompt `s` (where `s` is a string) and returns the user's response: 

```python
x = input('Enter your name:') 
f'Hello, {x}'								# "Hello, {whatever the user inputted}"
```


## String methods

Python has a set of built-in methods that you can use on strings. Here are a few examples:

+ The `lower()` method returns the string in lower case:

```python
a = "Hello, World!"
a.lower()									# "hello, world!"
```

+ The `upper()` method returns the string in upper case:

```python
a = "Hello, World!"
a.upper()									# "HELLO, WORLD!"
```

+ The `replace()` method replaces a string with another string:

```python
a = "Hello, World!"
a.replace("H", "J")							# "JELLO, WORLD!"
```

+ The `split()` method splits the string into a list of substrings if it finds instances of the separator:

```python
a = "Hello, World!"
a.split(",")								# ['Hello', ' World!']
```



# THE BOOL TYPE

## Two types of bools

There are two types of booleans: `True` and `False`. They exist to represent statements that are true and false.

```python
type(True)						       # class: bool
type(False)						       # class: bool
```


## Basic boolean operators

`not`, `and`, and `or` are the most basic boolean operators. You can use these to combine booleans and manipulate boolean logic.

```python
not True                          # False

True and True					            # True
True and False					          # False
False and False					          # False

True or True						          # True
False or True					            # True
False or False					          # False

True and False or True			      # What would this be?
```


## Implicit type conversions

As with everything else, python is able to convert other types into bools. The logic behind it is, the most basic version of each type gets converted to `false`, while any other version of that type is `true`. For example, for `int`, `bool(0)` is `false`, while any other `int` would be converted to `true`. Similarly, `bool("")` is false, while any other string would be converted to `true`. 

Additionally, we can see from the last example that python does implicit conversions -- when you put any other type into a function used for booleans, it will automatically convert that type into a boolean. **Note: try not to use logic like this in your code, as it is very non-intuitive to read and understand.**

```python
bool(-5)							            # True
bool(0)							              # False
bool("")							            # False
bool("hello")					            # True
bool(None)						            # False

5 or "hello" and None			        # False
```


## Conditionals

One useful way that python uses booleans is in conditionals: If a certain condition is met, python will do something; otherwise, python will do something else. You can use the following notation:

```
if {condition1}:
  statement1
elif {conditon2}:
  statement2
elif {condition3}: 
  statement3
...
elif {conditonN}:
  statementN
else:
  statementM
```

where python will evaluate exactly one of the statements based on the first condition to evaluate to `true`. Note that you don't need all of this for valid code; if there are only two options, then `if ... else ...` is sufficient, while if there is only one condition then just an `if ...` may be good enough. Here's an example:

```python
def waterState(tempC):
  if tempC >= 100:
    print("The water is boiling!")
  elif tempC <= 0:
    print("The water is frozen!")
  else:
    print("The water is a liquid.")

waterState(150)                   # The water is boiling!
waterState(30)                    # The water is a liquid.
waterState(-1)                    # The water is frozen!
```
