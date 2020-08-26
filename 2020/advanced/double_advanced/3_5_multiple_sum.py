def sumMult3And5(n):
    if n == 0:
        return 0
    elif n % 3 == 0 or n % 5 == 0:
        return n + sumMult3And5(n - 1)
    else:
        return sumMult3And5(n - 1)

def sumMult3And5CPS(n, k = lambda x : x):
    if n == 0:
        return k(0)
    elif n % 3 == 0 or n % 5 == 0:
        return sumMult3And5CPS(n - 1, lambda x : n + k(x))
    else:
        return sumMult3And5CPS(n - 1, k)

print(sumMult3And5CPS(1000))