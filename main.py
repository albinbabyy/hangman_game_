import random

word_list = ["aardvark" , "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

display = []
for space in range(word_length -1):
    display += "_"
print(display)

guess = input("Enter your guess letter : \n").lower()

# to find the "postition" and need to insert letter in "dispaly".
for position in range(word_length -1):
    letter = chosen_word[position ]
    if letter == guess:
        display[position] = letter
print(display)




