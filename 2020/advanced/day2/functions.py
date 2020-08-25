#======================== EXAMPLES ========================
def isEven(n):
  return n % 2 == 0

def isOdd(n):
  return n % 2 == 1

#======================== SCOPE ========================
def f(x):
  print("x:", x)
  y = 5
  print("y:", y)
  return x + y
print(f(4))
print(x) # will crash!
print(y) # would also crash if we reached it!

def g(x):
  print("In f, x =", x)
  x += 5
  return x

def h(x):
  y = f(x*2)
  print("In g, x =", x)
  z = f(x*3)
  print("In g, x =", x)
  return y + z

print(h(2))

#======================== RETURN ========================
def isPositive(x):
  # print("Hello!")   # runs
  return (x > 0)
  # print("Goodbye!") # does not run ("dead code")

print(isPositive(5))  # prints Hello, then True

def f(x):
    result = x + 42

print(f(5)) # None

#======================== PRINT VS RETURN ========================
def cubed(x):
  print(x**3) # Here is the error!
  # return (x**3) # That's better!

# We commonly write functions to solve problems.
# We can also write functions to store an action that is used multiple times!
# These are called helper functions.


#======================== HELPER FUNCTIONS ========================
def onesDigit(n):
    return n%10

def largerOnesDigit(x, y):
    return max(onesDigit(x), onesDigit(y))

print(largerOnesDigit(134, 672)) # 4
print(largerOnesDigit(132, 674)) # Still 4

cubed(2)          # seems to work!
print(cubed(3))   # sort of works (but prints None, which is weird)
print(2*cubed(4)) # Error!

def isPrime(n): 
  if (n <= 1):
    return False
  if (n == 2):
    return True
  for i in range (2, n):
    if n % i == 0:
      return False
  return True