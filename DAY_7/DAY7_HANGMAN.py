#DAY-7

import random
from hangmanwordlist import word_list
from hangaman_ascii import stages

chosen_word=random.choice(word_list)

#print(chosen_word)

lives=6

display=[]
word_length=len(chosen_word)

for _ in range(word_length):
    display+='_'

print(f"{' '.join(display)}")
game_over=False
while not game_over:
    user_input=input('Guess the word: ').lower()
    
    for position in range(word_length):
        letter=chosen_word[position]
        if letter == user_input:
            display[position]=letter
    if user_input not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print('You Lose')
            print(f'The correct word is {chosen_word}')
        print(stages[lives])
    print(f"{' '.join(display)}")
    if'_' not in display:
        game_over=True
        print('you won')
        