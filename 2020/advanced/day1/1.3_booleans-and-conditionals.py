#============================  TWO TYPES OF BOOLS  ============================

print(type(True))						      # class: bool
print(type(False))						    # class: bool


#=========================  BASIC BOOLEAN OPERATORS  ==========================

# print(not True)                   # False

# print(True and True)					    # True
# print(True and False)					    # False
# print(False and False)					  # False

# print(True or True)						    # True
# print(False or True)					    # True
# print(False or False)					    # False

# print(True and False or True)			# What would this be?

# print(True or (5 != 5))
print(False and 1/0)
print(True or 1/0)


#========================  IMPLICIT TYPE CONVERSIONS  =========================

# Note: Try not to use this in your code!!!
# print(bool(-5))							      # True
# print(bool(0))							      # False
# print(bool(""))							      # False
# print(bool("hello"))					    # True
# print(bool(None))						      # False

# print(5 or "hello" and None)			# What might this be?


#===============================  CONDITIONALS  ===============================

# def waterState(tempC):
#   if tempC >= 100:
#     print("The water is boiling!")
#   elif tempC <= 0:
#     print("The water is frozen!")
#   else:
#     print("The water is a liquid.")

# waterState(150)                   # The water is boiling!
# waterState(30)                    # The water is a liquid.
# waterState(-1)                    # The water is frozen!

# Let's try solving a problem!
# https://projecteuler.net/problem=1








