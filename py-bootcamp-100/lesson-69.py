import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

wrk_list = []
for idx in range(0, len(chosen_word)):
   wrk_list.append("_")

guess = input("Enter a letter: ").lower()[0]

guess_idx = chosen_word.find(guess)
if guess_idx > -1:
    wrk_list[guess_idx] = guess
    print(f"Found {guess} at {guess_idx}")
else:
    print("Not Found")

print(chosen_word, " ", guess, "\n")

print(wrk_list)