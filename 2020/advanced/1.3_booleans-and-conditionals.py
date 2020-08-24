# This file touches upon booleans, equality, and conditionals

#============================  TWO TYPES OF BOOLS  ============================

print(type(True))						      # class: bool
print(type(False))						    # class: bool


#=========================  BASIC BOOLEAN OPERATORS  ==========================

print(True and True)					    # True
print(True and False)					    # False
print(False and False)					  # False

print(True or True)						    # True
print(False or True)					    # True
print(False or False)					    # False

print(True and False or True)			# What would this be?


#========================  IMPLICIT TYPE CONVERSIONS  =========================

# Note: Try not to use this in your code!!!
print(bool(-5))							      # True
print(bool(0))							      # False
print(bool(""))							      # False
print(bool("hello"))					    # True
print(bool(None))						      # False

print(5 or "hello" and None)			# What might this be?


#===============================  CONDITIONALS  ===============================

def waterState(tempC):
  if tempC >= 100:
    print("The water is boiling!")
  elif tempC <= 0:
    print("The water is frozen!")
  else:
    print("The water is a liquid.")

waterState(150)
waterState(30)
waterState(-1)
waterState("3")










