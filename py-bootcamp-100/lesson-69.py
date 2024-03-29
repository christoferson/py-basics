import random

from lessonlib import cmn_word_list

chosen_word = random.choice(cmn_word_list)

# Initialize work array with underscore
wrk_list = []
for idx in range(0, len(chosen_word)):
   wrk_list.append("_")

end = True
guess_count = 0
guess_max = len(chosen_word) + 5

for cnt in range (0, guess_max):

    guess = input(f"Enter a letter {guess_count}/{guess_max}: ").lower()[0]
    guess_count += 1

    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            wrk_list[i] = guess

    print(chosen_word, " ", guess, "\n")

    print(wrk_list)

    # Check if work array still contains "_"
    for wrk in wrk_list:
        if wrk == "_":
            end = False
        else:
            end = True
    print("End: " , end)

    if end == True:
        print(f"Congratulations! Answer: {chosen_word} Guess: {guess_count}")
        break
    else:
        if guess_count == guess_max:
            print(f"Out of luck! Answer is {chosen_word}.")
        else:
            print(f"{guess_max - guess_count} guesses left.")