#DAY-12
from random import randint
from art import logo 
EASY=10
HARD=5
def check(guess,answer,turns):
    """check the answer and returns the turns remaining"""
    if guess>answer:
        print('TOO HIGH')
        return turns-1
    elif guess<answer:
        print('TOO LOW')
        return turns-1
    else:
        print(f'Yes you got it, the correct answer is : {answer}')
def set_level():
    user_level = input('Do you want EASY or HARD level!? : ')
    if user_level=='easy':
        return EASY
    else:
        return HARD
def game():
    print(logo)
    print('WELCOME TO THE NUMBER GUESSING GAME !')
    print("\nGuess a Number from 1 to 100")
    answer=randint(1,100)
    print(f"PSST ! Your answer is {answer}")
    turns=set_level()
    guess=0
    while guess!=answer:
        print(f"You have {turns} remaning !") 
        guess=int(input('Guess the number : '))
        turns=check(guess,answer,turns)
        if turns==0:
            print('You ran out of guesses, You Lose')
            print(f"\nThe Correct answer was {answer}")
        else:
            guess!=answer
            print('Guess again')
game() 