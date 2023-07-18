
print(type(3.33))

str = str(3.33)
print(type(str))
print(type(float(33)))

two_digit_number = input("Enter 2 digit number: ")
if (len(two_digit_number) != 2):
  print("Error. Enter a 2 digit number.")
elif (two_digit_number.isdigit() == False):
  print("Error. value is not a number.")
else:
  sum = int(two_digit_number[0]) + int(two_digit_number[1])
  print(sum)