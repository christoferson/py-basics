# Input
print("Hi " + input("Enter Name: "))

# Challenge
print("Hi-L1 " + str(len(input("Enter Name: "))))

# Variable
name = input("Enter Name: ")
print("Hi-L2 " + str(len(name)))

# Challenge
a = input("A: ")
b = input("B: ")

tmp = a
a = b
b = tmp

print("A: " + a + " B: " + b) 

# Final Challenge

print("Welcome to the Band Name generator!")
city = input("What is the name of the city you grew up in? \n")
pet = input("What is the name of your pet? \n")
print(city + " " + pet)