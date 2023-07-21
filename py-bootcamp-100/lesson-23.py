# Truncate Decimals
print(int(8/3))

# Round
print(round(8/3))

# Round
print(round(8/3, 2))

# BMI Calculator
weight = input("Input Weight (kg): ")
height = input("Input Height (m): ")

bmi = int(weight) / (float(height) ** 2)
bmi = round(bmi, 0)

print("BMI: " + str(bmi));