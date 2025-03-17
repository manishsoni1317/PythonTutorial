# sum(8) = 1+2+3+4+5+6+7+8 = 36
# sum(n) = n + sum(n-1) if n > 0
n = 8
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
    

print(sum(n))