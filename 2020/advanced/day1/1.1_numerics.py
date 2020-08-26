#==============================  BASIC EXAMPLES  ==============================

print(type(5)) 					# class: int
print(isinstance(-3, int))		# True
print(type(0.5)) 				# class: float

print(type(5.0)) 				# what will this print?


#===============================  CONVERSIONS  ================================

# x = 5
# y = 4.0
# z = 6.5

# print(float(x)) 				# 5.0
# print(int(y))					# 4
# print(int(z))					# 6 -- Note: just drops the decimal, not rounding
# print(x + y)					# what will this print? hint: implicit conversions


#================================  COMPARISON  ================================

# print(5 == 5) 				# True
# print(5.0 == 5.0) 			# True
# print(5 == 4)				    # False
# print(5 == 5.0)				# True
# print(5 < 6)					# True
# print(-1 > 0)					# False

## Note: <, >, <=, >= can all be used similarly


#================================  ARITHMETIC  ================================

# print(5 + 3)					# 8
# print(9 - 6)					# 3
# print(3 * 21)					# 63
# print(10 / 3)					# 3.33333
# print(10 // 3)				# 3
# print(9 // 3)					# 3
# print(9 / 3)					# 3.0
# print(100 % 3)				# 1
# print(4 + 3 * 2)				# Note: Remember PEMDAS!!


#=========================  OTHER BUILT-IN FUNCTIONS  =========================

# print(abs(-5))   				# absolute value
# print(max(2, 3))  			# return the max value
# print(min(2, 3))  			# return the min value
# print(pow(2, 3))  			# raise to the given power (pow(x,y) == x**y)
# print(round(2.354, 1)) 		# round with the given number of digits


#===========================  USING THE MATH LIBRARY  ==========================

# import math

# print(math.sin(0))				# math.cos, math.tan, math.asin, etc.
# print(math.floor(6.3))			# math.ceil exists also
# print(math.sqrt(25))			    # natural square root
# print(math.log(math.e))			# default natural log, but can add base: math.log(4, 2) == 2
# print(round(math.e, 3))			# e
# print(round(math.pi, 3))		    # pi

## Note: see https://docs.python.org/3/library/math.html for more functions


#===================================  ERRORS  =================================

# import math

# print(math.sqrt(-1))              # will not run!
# print(1/0)                        # will not run!