def encoder(password):
    
    new_p = ""
    
    for digit in password:
        new_d = str((int(digit) + 3) % 10)
        new_p += new_d
    return new_p

def decoder(password):
    decoded_pass = ''
    for n in password:
        decoded_pass += str(int(n) - 3)

    return decoded_pass


def main():
    
    while True:

        
        option = input("Please enter an option: ")
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        
        if option == 1:
            pass
        if option == 2:
            decoded_pass = decoder(encoder(password))
            print("The encoded password is" + encoder(password) + ", and the original password is " + decoded_pass)


        option = input("Please enter an option: ")

