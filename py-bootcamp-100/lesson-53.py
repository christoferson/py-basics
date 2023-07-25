import random

# Loop from 1 to 10
for number in range(1, 10):
    print(number)

# Loop from 1 to 10 increment by 2
for number in range(1, 10, 2):
    print(number)

# Excercise - Sum Even Numbers
total = 0
for number in range(2, 101, 2):
    total = total + number
print(f"Sum: {total}")

# Fizz Buzz
for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
num_letters = int(input(f"How many letters? ")) 
num_symbols = int(input(f"How many symbols? "))
num_numerals = int(input(f"How many numerals? "))

password_characters = []

for char in range(1, num_letters + 1):
  password_characters.append(random.choice(letters))

for char in range(1, num_symbols + 1):
  password_characters += random.choice(symbols)

for char in range(1, num_numerals + 1):
  password_characters += random.choice(numbers)

print(password_characters)
random.shuffle(password_characters)
print(password_characters)

password = ""
for char in password_characters:
  password += char

print(f"Your password is: {password}")