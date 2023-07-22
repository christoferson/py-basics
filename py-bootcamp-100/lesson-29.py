# Conditional Statement

#if condition:
#    foo
#else:
#    bar

# Excercise - Theme Park

height = int(input("what is your height in centimeters? "))
if height >= 120:
    if height == 120:
        print("great, you made it")
    else:
        print("welcome aboard")
else:
    print("better luck next time")

# Excercise - Odd or Even

print("Odd or Even /n")
number = int(input("Enter a number: "))
if (number % 2) == 0:
    print("Even")
else:
    print("Odd")

# 
age = int(input("what is your age? "))
if age <= 8:
    print("Pay $5")
elif age <= 12:
    print("Pay $8")
elif age <= 18:
    print("Pay $12")
else:
    print("Pay $18")