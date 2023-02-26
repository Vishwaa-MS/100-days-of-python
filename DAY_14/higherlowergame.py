#DAY-14
from random import choice
from gamedata import data
from art import logo,vs
from replit import clear
print(logo)

score=0
def format_acc(account):
    acc_name=account['name']
    acc_des=account['description']
    acc_country=account['country']
    return f"{acc_name}, a {acc_des}, from {acc_country}"
def check(guess,a_follower,b_follower):
    if a_follower>b_follower:
        return guess=='a'
    else:
        return guess=='b'
acc_b=choice(data)

should_continue=True

while should_continue:
    acc_a=acc_b
    acc_b=choice(data)
    while acc_a==acc_b:
        acc_b=choice(data)             
    print(f"compare A: {format_acc(acc_a)}")
    print(vs)
    print(f"Against B: {format_acc(acc_b)}")
    guess=input('who has more followers. Type A or B: ').lower()    
    a_follower=acc_a['follower_count']
    b_follower=acc_b['follower_count']   
    is_correct=check(guess, a_follower, b_follower)
    clear()
    print(logo)
    if is_correct:
        score+=1
        print(f"Yes you got it right and your current score is {score}")
        
    else:
        should_continue=False
        print(f"OOPS that's wrong and your final score is {score}")
