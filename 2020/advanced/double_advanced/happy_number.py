def sumOfSquareDigits(n): return 0 if n == 0 else (n % 10) ** 2 + sumOfSquareDigits(n // 10)

def isHappyNumber(n, cache = []):
    if n == 1:
        return True
    elif n in cache:
        return False
    else:
        return isHappyNumber(sumOfSquareDigits(n), cache + [n])

