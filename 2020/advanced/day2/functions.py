
#======================== LOOPS ========================

# def sumFromMToN(m, n):
#     total = 0
#     # note that range(x, y) includes x but excludes y
#     for x in range(m, n+1):
#         total += x #total = total + x
#     return total

# print(sumFromMToN(5, 10) == 5+6+7+8+9+10)

# def printCoordinates(xMax, yMax):
#    for x in range(xMax+1):
#        for y in range(yMax+1):
#            print("(", x, ",", y, ")  ", end="")
#        print()

# printCoordinates(4, 5)

# def printStarRectangle(n):
#     #print an nxn rectangle of asterisks
#    for row in range(n):
#        for col in range(n):
#            print("*", end="")
#        print()

# printStarRectangle(5)


#======================== WHILE ========================
# def leftmostDigit(n):
#    n = abs(n)
#    while (n >= 10):
#        n = n//10
#    return n

# print(leftmostDigit(72658489290098) == 7)


#======================== EXAMPLES ========================
# def isEven(n):
#   return n % 2 == 0

# def isOdd(n):
#   return n % 2 == 1

#======================== SCOPE ========================
# x = 2
# def f(x):
#  print("x:", x)
#  y = 5
#  print("y:", y)
#  return x + y
# print(f(4))
# print(x) # will crash!
# print(y) # would also crash if we reached it!

# def g(x):
#  print("In f, x =", x)
#  x += 5
#  return x

# def h(x):
#  y = f(x*2)
#  print("In g, x =", x)
#  z = f(x*3)
#  print("In g, x =", x)
#  return y + z

# print(h(2))

#======================== RETURN ========================
# def isPositive(x):
#   print("Hello!")   # runs
#   return (x > 0)
#   print("Goodbye!") # does not run ("dead code")

# print(isPositive(5))  # prints Hello, then True

# def f(x):
#    result = x + 42
#    return result

# print(f(5)) # None

#======================== PRINT VS RETURN ========================
# def cubed(x):
#   print(x**3) # Here is the error!
#   # return (x**3) # That's better!

# cubed(3)
# print(cubed(3))

#cubed(2)          # seems to work!
#print(cubed(3))   # sort of works (but prints None, which is weird)
#print(2*cubed(4)) # Error!

# We commonly write functions to solve problems.
# We can also write functions to store an action that is used multiple times!
# These are called helper functions.


#======================== HELPER FUNCTIONS ========================
#def onesDigit(n):
#    return n%10

#def largerOnesDigit(x, y):
#    return max(onesDigit(x), onesDigit(y))

#print(largerOnesDigit(134, 672)) # 4
#print(largerOnesDigit(132, 674)) # Still 4

def isPrime(n): 
 if (n <= 1):
   return False
 if (n == 2):
   return True
 for i in range (2, n):
   if n % i == 0:
     return False
 return True