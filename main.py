import random

word_list = ["aardvark" , "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

display = []
for space in range(word_length ):
    display += "_"
print(display)


end_of_game = False
while not False:

    guess = input("Enter your guess letter : \n").lower()

    # to find the "postition" and need to insert letter in "dispaly".
    for position in range(word_length ):
        letter = chosen_word[position ]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you won")

        break



