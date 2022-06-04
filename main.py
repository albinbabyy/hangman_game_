import random

word_list = ["aardvark" , "baboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

guess = input("Enter your guess letter : \n").lower()

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("flase")
