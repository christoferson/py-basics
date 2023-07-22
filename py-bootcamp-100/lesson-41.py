import random

# Genrate Random Int
rint = random.randint(0, 5)
print(rint)

# Genrate Random Float
rfloat = random.random()
print(int (rfloat * 5))

list1 = [1, 2, 3]
list2 = ["apple", "orange", "banana"]
list3 = [1, "apple", 2, False]
print(list3[1])
print(list3[-1])

list3[0] = "foo"
print(list3[0])

list3.append("bar")
print(list3)

# Challenge
str = "Mark,Angela,Ben,Jenny,Jack"
arr = str.split(",")
idx = random.randint(0, len(arr)-1)
print(arr[idx] + " selected")
# Using Choice
print(random.choice(arr) + " selected")
