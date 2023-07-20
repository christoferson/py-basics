weight = input("Input Weight (kg): ")
height = input("Input Height (m): ")

bmi = int(weight) / (float(height) ** 2)
bmi = round(bmi, 0)

print("BMI: " + str(bmi));