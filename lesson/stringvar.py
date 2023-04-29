# string
foo = "barzooper"
print(len(foo))

bar = "hello \n world"
print(bar)


# Indexing
print(foo[1])

# Reverse Indexing
print(foo[-1])

# Slicing
string1 = "abcdefghijklm"
print(string1[3:]) # starts from letter d till the end
print(string1[:5]) # all letters till e
print(string1[2:5]) # c till e
print(string1[::]) # grab everything
print(string1[::2]) # grab everything in steps of 2
print(string1[::-1]) # reverse the string