# Enclosed by square brackets. Separated by comma
mylist_numbers = [1,2,3,4,5]
print(mylist_numbers)
mylist_mix = ["str", 5, 3.7]
print(mylist_mix)
print(len(mylist_mix))

# index
mylist = ["one", "two", "three", "four", "five"]
print(mylist[0])

# slicing
print(mylist[2:])

# concatenate
print([1,2] +[3,4])

# mutate element
mylist[0] = "ten"
print(mylist)

# append
mylist.append("six")
print(mylist)

# remove last item
item = mylist.pop()
print(mylist)
print(item)

# remove item at
item = mylist.pop(0)
print(mylist)
print(item)

# sort
mylist = ["a", "e", "c", "b", "d"]
print(mylist)
nlist = mylist.sort()
print(mylist)
print(nlist, type(nlist))

# reverse
mylist.reverse()
print(mylist)

# nested list
nestedlist= [1,1,[1,2]]
print(nestedlist)
print(nestedlist[2][1])
