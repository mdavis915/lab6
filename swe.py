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
        new_d = str((int(digit) + 3) % 10)
        new_p += new_d
    return new_p

# Decodes the encoded password and returns the original password
def decoder(password):
    decoded_pass = ''
    for n in password:
        decoded_pass += str(int(n) - 3) #FIXME

    return decoded_pass

# Prints the menu
def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit ")
    print()


def main():
    
    password = ""
    menu()
    option = input("Please enter an option: ")
    
    while True:
        # If the user chooses 1, it encodes the password they entered
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        # If the user chooses 2, it ouputs the encoded password and the original password
        elif option == 2:
            pass
            #FIXME
        elif option == 3:
            pass
            #FIXME
        else:
            pass
            #FIXME

        menu()
        option = input("Please enter an option: ")
        
if __name__ == '__main__':
    main()

