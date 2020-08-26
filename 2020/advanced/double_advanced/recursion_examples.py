#=============================  Factorial Example =============================

def factorial(n):
    res = 1
    for i in range(n):
        res *= (i+1)
    return res

def factorialRecursive(n): return n * factorialRecursive(n - 1) if n > 1 else 1


#=============================  List Sum Example ==============================

def listSum(L):
    res = 0
    for i in L:
        res += i
    return res

def listSumRecursive(L): return L[0] + listSumRecursive(L[1:]) if len(L) > 0 else 0

def listSumDivideAndConquer(L):
    if len(L) < 1: return 0
    elif len(L) == 1: return L[0]
    return listSumDivideAndConquer(L[:len(L)//2]) + listSumDivideAndConquer(L[len(L)//2:])

