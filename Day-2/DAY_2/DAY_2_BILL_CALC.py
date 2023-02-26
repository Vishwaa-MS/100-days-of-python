#SPLIT BILL AND TIP CALCULATOR
print('Welcome to the Calculator !')
bill=float(input('What was the total bill? : '))
tip=int(input('What percentage TIP would you like to give? : '))
split=int(input('How many people to split the bill? : '))

tip_to_pay=bill*(tip/100)
total_bill= bill+tip_to_pay
bill_each_to_pay=total_bill/split
final_amt=round(bill_each_to_pay,2)
print(f'\nThe amount to be paid by each is {final_amt}')

