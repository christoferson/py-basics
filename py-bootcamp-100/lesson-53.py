
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