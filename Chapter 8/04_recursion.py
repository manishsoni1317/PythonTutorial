'''
factorial(0) = 1 by definition
factorial(n) = n * factorial(n-1) if n > 0
factorial(4) = 4 * 3 * 2 * 1 = 24
factorial(3) = 3 * 2 * 1 = 6
'''
n = 7
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(n))