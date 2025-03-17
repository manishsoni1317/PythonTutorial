from functools import reduce
# Demonstration for Map
square = lambda x: x*x
l = [1,2,3,4,5,6]
c = map(square,l)
print(list(c))


# Demonstration for filter
greater = lambda x: x>4
a= [1,2,3,4,5,6,54,67,89,8,25]
d = filter(greater, a)
print(list(d))

# Demonstration for Reduce
sum = lambda x, y: x+y
a = [1,2,3,7]
d = reduce(sum, a)
print(d)
