# For Loop

fruits = ["apple", "orange", "banana", "strawberry"]

for fruit in fruits:
    print(fruit)

# Calculate the average

numbers = [87, 83, 17, 53, 23, 37, 23]

sum = 0
cnt = 0
for number in numbers: 
    sum += number
    cnt += 1

avg = round(sum / cnt, 2)
print(f"Average: {avg}")