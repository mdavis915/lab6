def encoder(password):
    
    new_p = ""
    
    for digit in password:
        new_d = str((int(digit) + 3) % 10)
        new_p += new_d
    return new_p


def main():
    
    while True:

        
        option = input("Please enter an option: ")
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        
        if option == 1:
            pass

        print("Hello")