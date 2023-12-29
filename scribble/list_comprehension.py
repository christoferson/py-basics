fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# [expression for item in iterable if condition == True]
selection = [x for x in fruits if "a" in x]
print(selection)