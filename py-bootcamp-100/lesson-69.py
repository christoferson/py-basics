import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Enter a letter: ").lower()[0]

if chosen_word.find(guess) > -1:
    print("Found")
else:
    print("Not Found")

print(chosen_word, " ", guess)