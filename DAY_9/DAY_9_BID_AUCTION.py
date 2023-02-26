from asciibid import logo
from replit import clear

print(logo)

new_dict={}

def high_bid(bid_records):
    highest=0
    for bidder in bid_records:
        bid_amt=bid_records[bidder]
        if bid_amt>highest:
            highest=bid_amt
            winner=bidder
    print(f"\nThe Winner is {winner} with bid amount of ${highest}")
       
    
continues_done=False
while not continues_done:
    name=input('What is your name? : ')

    bid=int(input('What is your BID? : $'))

    new_dict[name]=bid
    cont=input('Are there any other bidders!?, Type "yes or "no\n')
    
    if cont=='no':
        continues_done=True
        high_bid(new_dict)
    elif cont=='yes':
        clear()
print(new_dict)