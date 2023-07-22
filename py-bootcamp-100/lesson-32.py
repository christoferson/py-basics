# BMI Calculator 2.0
weight = input("Input Weight (kg): ")
height = input("Input Height (m): ")

bmi = float(weight) / (float(height) ** 2)
bmi = round(bmi, 0)

print("BMI: " + str(bmi));

if bmi <= 18.5:
    print("underweight")
elif bmi <= 25:
    print("normal weight")
elif bmi <= 30:
    print("overweight")
elif bmi <= 35:
    print("obese")
else:
    print("clinically obese")

# Leap Year
year = 2400

if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
          print("leap year")
      else:
          print("not div by 400, not leap year")      
    else:
      print("leap year")
else:
    print("not div by 4, not leap year")

#  Pizza Price
pizza_size = input("Enter Pizza Size (S/M/L): ")
want_pepperoni = input("Pepperoni? (Y/N): ")
want_cheeze = input("Cheeze? (Y/N): ")
cost = 0

if pizza_size == "S":
    cost += 15
elif pizza_size == "M":
    cost += 20
elif pizza_size == "L":
    cost += 25

if want_pepperoni == "Y":
    if pizza_size == "S":
      cost += 2
    else:
      cost += 3

if want_cheeze == "Y":
    cost += 1

print(f"Pizza cost: ${cost}")

   