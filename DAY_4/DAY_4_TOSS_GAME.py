import random

random_coin= random.randint(1,2)

print('This is a coin toss game.')
choose=(input('Choose if tou want "Heads" or "Tails"\n')).lower()

if choose == 'heads': 
    a=1
else: 
    a=2

if random_coin == 1: 
    print('Heads\n')
else: 
    print('Tails\n')
if a== random_coin : 
    print('YOU WIN!!!!!')
else: 
    print('YOU LOSE!')
    


 