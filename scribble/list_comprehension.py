fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# [expression for item in iterable if condition == True]
selection = [x for x in fruits if "a" in x]
print(selection)

selection = [x.upper() for x in fruits] 
print(selection)

# Return the item if it is not banana, if it is banana return orange
selection = [x if x != "banana" else "orange" for x in fruits] 
print(selection)

numbers = [x for x in range(10) if x < 5] 
print(numbers)

