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

# Immutability
immutablestr = "Foo"
#immutablestr[0] = "B" # TypeError: 'str' object does not support item assignment

# String concatenation
print("B" + immutablestr[1::])

# String multiplication
print("z" * 10)

# Plus Operator and Operand Types
print(3 + 5) # prints 8
print('3' + '5') # prints 35

strx = "foo Bar|zap Kap"
print(strx.upper())
print(strx.lower())
print(strx.split())
print(strx.split("|"))

# Printing Formatting and Printing / Interpolation
stry = "foo {} bar {} zoom {}"
print(stry.format("A", "B", "C"))
print("foo {0} bar {1} zoom {2}".format("A", "B", "C")) # default
print("foo {2} bar {1} zoom {0}".format("A", "B", "C")) # index
print("foo {b} bar {c} zoom {a}".format(a="A", b="B", c="C")) # keywords

# Formatting Floating Numbers
mfloat = 100/777
print("100/777={f:1.5f}".format(f=mfloat))

# f strings
print(f"100/777={mfloat:1.5f}")