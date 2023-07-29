import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

wrk_list = []
for idx in range(0, len(chosen_word)):
   wrk_list.append("_")

end = True

for cnt in range (0, 10):

    guess = input("Enter a letter: ").lower()[0]

    """
    guess_idx = chosen_word.find(guess)
    if guess_idx > -1:
        wrk_list[guess_idx] = guess
        print(f"Found {guess} at {guess_idx}")
    else:
        print("Not Found")
    """

    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            wrk_list[i] = guess


    print(chosen_word, " ", guess, "\n")

    print(wrk_list)


    for wrk in wrk_list:
        if wrk == "_":
            end = False
        else:
            end = True
    print("End: " , end)

    if end == True:
        break