#DAY-8
#ENCRYPTION AND DECRYPTION
from art import logo,bye
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c',
            'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caeser(start_text, shift_amt, cipher_direction):
    end_text=''
    if cipher_direction == 'decode':
        shift_amt*=-1
    
    for char in start_text:
        if char in alphabet:
            position= alphabet.index(char)
            new_position= position + shift_amt
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"The {cipher_direction}d is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift%26
    
    caeser(start_text=text, shift_amt=shift, cipher_direction=direction)

    result = input("Type 'yes' to Continue 'no' to Exit !\n")
    
    if result == 'no':
        should_continue = False
        print("\n",bye)






























# def encrypt(plain_text, shift_amt):
#     cipher_text=""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amt
#         new_letter = alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"YOUR ENCRYPTED MESSAGE IS {cipher_text}")




# def dencrypt(encrpted_text, shift_amt):
#     plan_text=""
#     for letter in encrpted_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amt
#         new_letter = alphabet[new_position]
#         plan_text+=new_letter
#     print(f"YOUR DENCRYPTED MESSAGE IS {plan_text}")



# if direction == 'encode':
#     encrypt(plain_text=text, shift_amt=shift)
# elif direction == 'decode':
#     dencrypt(encrpted_text=text, shift_amt=shift)
# else:
#     print("Enter the valid Input")