score = 2

msg = f"Score is {score}"
print(msg)

# Challenge - Life Remaining
age = int(input("What is your age: "))

remain_years = 90 - age
days = remain_years * 365
weeks = remain_years * 52
months = remain_years * 12

print(F"Years: {remain_years} Days: {days} Weeks: {weeks} Months: {months}")

# Challenge - Tip Calculator
total_bill = float(input("Total Bill: "))
tip_percent = int(input("Tip % (10,12,15): "))
party_size = int(input("Party Size: "))

total_bill = total_bill * (1 + (tip_percent/100))
bill_per_person = round(total_bill / party_size, 2)
print(f"Per Person: {bill_per_person}")