#DAY_11
import random
from replit import clear
from art import logo
def card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        return cards
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return 'Draw :|'
    elif computer_score == 0:
        return "LOST, Opponent won BLACKJACK !"
    elif user_score == 0:
        return "YOU WON WITH A BLACKJACK !"
    elif user_score>21:
        return 'You went over, YOU LOST'
    elif computer_score>21:
        return 'Opponent went Over, YOU WON'
    elif user_score>computer_score:
        return "You WON !"
    else: 
        return 'You LOSE !'  

def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    for _ in range(2):
        user_cards.append(card())
        computer_cards.append(card())
        
    is_game_over=False
    while not is_game_over:    
        #calculate_score(user_cards)
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your card: {user_cards}, Current score {user_score}")
        print(f"\ncomputers first card: {computer_cards[0]}")
        
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_deal=input('Type Y to get an another card or N to pass: ')
            if  user_deal=='y':
                user_cards.append(card())
            else:
                is_game_over=True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(card())
        computer_score=calculate_score(computer_cards)
    print(f"\nYour handle: {user_cards}, Final score: {user_score}")
    print(f"\ncomputer's handle: {computer_cards}, Final Score: {computer_score}")
    print(compare(user_score,computer_score))   

while input("Do you want to play BLACKJACK GAME type 'y' or 'n': ")=='y':
    clear()
    play_game()