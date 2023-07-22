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

# Leap Year - V2
year = 2400

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("leap year")
else:
    print("not div by 4, not leap year")

# Love Calculator

him = input("His Name: ")
her = input("Her Name: ")

# Version 1

him = him.lower()
her = her.lower()

count_true = 0
count_true += him.count("t") + him.count("r") + him.count("u") + him.count("e")
count_true += her.count("t") + her.count("r") + her.count("u") + her.count("e")

count_love = 0
count_love += him.count("l") + him.count("o") + him.count("v") + him.count("e")
count_love += her.count("l") + her.count("o") + her.count("v") + her.count("e")

print(f"{count_true} {count_love} {str(count_true) + str(count_love)}")

# Version 2

pair = him.lower() + her.lower()

t = pair.count("t")
r = pair.count("r")
u = pair.count("u")
e = pair.count("e")
sum_true = t + r + u + e 

l = pair.count("l")
o = pair.count("o")
v = pair.count("v")
e = pair.count("e")
sum_love = l + o + v + e

print(f"t={t} r={r} u={u} e={e} {sum_true}")
print(f"l={l} o={o} v={v} e={e} {sum_love}")
print(f"{sum_true}{sum_love}")

love_score = int(str(sum_true) + str(sum_love))
if (love_score > 10 and love_score < 90):
    print(f"Your score is {love_score}, you go together like coke and methos")
elif (love_score > 40 and love_score < 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
