import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
lives = 6

display = []
for space in range(word_length ):
    display += "_"
print(display)


end_of_game = False
while not False:

    guess = input("Enter your guess letter : \n").lower()

    if guess in chosen_word:
        print("already guessed")
    # to find the "postition" and need to insert letter in "dispaly".
    for position in range(word_length ):
        letter = chosen_word[position ]
        if letter == guess:
            display[position] = letter

    print(f"{' ' .join(display)}")

    if guess not in chosen_word:

        lives -= 1
        print(f"you have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print("you lose")
            break

    if "_" not in display:
        end_of_game = True
        print("you won")

        break



