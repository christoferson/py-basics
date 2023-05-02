# Tuples

mytuple = (1, 2, 3)
print(type(mytuple))
print(mytuple)

# Element At
print(mytuple[1])

# Index
print(mytuple.index(3)) # Find first index of 3
#print(mytuple.index(5)) # Find first index of 5 # ValueError: tuple.index(x): x not in tuple

# Count
print(mytuple.count(2)) # Count occurence of 2
print(mytuple.count(5)) # Count occurence of 5 # returns 0

# Tuple is immutable
mytuple[0] = 5 #TypeError: 'tuple' object does not support item assignment