import random 
letter=  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
          'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
          'W', 'X', 'Y', 'Z']
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=["!","@","#","$","%","&","*"]

print('Welcome to PyPassword Generator!')

no_letter=int(input('How Many Letter Do You Want?: '))
no_symbols=int(input('How Many Symbols Do You Want?: '))
no_number=int(input('How Many Numbers Do You Want?: '))

pass_list=[]

for char in range(1,no_letter+1):
    pass_list.append(random.choice(letter))
for char in range(1,no_symbols+1):
    pass_list.append(random.choice(symbols))
for char in range(1,no_number+1):
    pass_list.append(random.choice(numbers))

random.shuffle(pass_list)

password=''
for char in pass_list:
    password += char
print(f'Your Password is: {password}')

