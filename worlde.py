
print("Welcome to Wordle!")
print("This is a game where you guess a five-letter word by other words and I am going to tell you if your letter are in the right place or are they even in the word.")
print("You get 10 guesses for each word.")

import random

with open("five_letter_words_in_english.txt","r") as file:
    words = list(map(str, file.read().split()))
    wordle_word = random.choice(words).lower()
    
dct = {0:"First letter",1:"Second letter",2:"Third letter",3:"Fourth letter",4:"Fifth letter"}



win = False

for turn in range(10):
    lst = [[],[],[],[],[]]
    correct_letters = 0
    guessed_word = input("Enter your word: ").lower()
    
    if len(guessed_word) != 5:
        print("Please enter a five-letter word.")
        continue
    
    for nr in range(5):
        if guessed_word[nr] in wordle_word:
            lst[nr].append("right letter")
            if guessed_word[nr] == wordle_word[nr]:
                lst[nr].append("right place")
                correct_letters += 1
    for i in range(len(lst)):
        if lst[i] != []:
            if len(lst[i]) == 1: 
                print(f"{dct[i]}: {lst[i][0]}!")
            else:
                print(f"{dct[i]}: {lst[i][0]} and {lst[i][1]}!")
                
    if correct_letters == 5:
        win = True
        break 

if win:
    print("Well done you guessed the word correctly!")
else:
    print(f"Game over. The word you were looking for was {wordle_word}. Better luck next time.")