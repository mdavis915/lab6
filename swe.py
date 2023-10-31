'''
Author: Maria Davis
Partner: Alexis Simpson
Assignment: Lab 6
Date Due: 11/31/2023
Class: COP3502, Section 12331
About: This program implements a a simplified password encoder/decoder program to practice the
functions of version control systems
'''

# Encodes password the user entered (numbers shifted by 3)
def encode(password):
    new_p = ""
    for digit in password:
        if int(digit) >= 7:
            new_d = str((int(digit) + 3) % 10)
        else:
            new_d = str(int(digit) + 3)
        new_p += new_d

    return new_p

# Decodes the encoded password and returns the original password
def decoder(password):
    decoded_pass = ''
    for n in password:
        if int(n) == 2:
            decoded_pass += 9
        elif int(n) == 1:
            decoded_pass += 8
        elif int(n) == 0:
            decoded_pass += 7
        else:
            decoded_pass += str(int(n) - 3)

    return decoded_pass

# Prints the menu
def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit ")
    print()


def main():
    
    password = ""
    menu()
    option = int(input("Please enter an option: "))
    
    while (option == 1) or (option == 2):
        # If the user chooses 1, it encodes the password they entered
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        # If the user chooses 2, it outputs the encoded password and the original password
        elif option == 2:
            decoded_password = decoder(encoded_password)
            print("The encoded password is " + encoded_password + ", and the original password is " + decoded_password + ".")
        menu()
        option = int(input("Please enter an option: "))
        
if __name__ == '__main__':
    main()

