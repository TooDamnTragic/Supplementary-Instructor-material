# import re
# def password_checker(input):
#     valid_password = False
#     length = len(input)
#     if length >=8 and length<=20:
#         valid_password = True
#     for char in input:
#         if char == " ":
#             valid_password = False
#     if valid_password = True:


# def main():
#     while True:
#         password = input("Enter password to check:")
#         if password_checker(password) == True:
#             print("Good password\n")
#             break
#         else:
#             print("Weak Password\n")

# if __name__ == "__main__":
#     main()




def password_checker(input):
    # Check length
    length = len(input)
    if length < 8 or length > 20:
        return False

    # Initialize flags for character types
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    # Define symbols (ASCII)
    symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

    # Check character types
    for char in input:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:  # 'a' to 'z'
            has_lower = True
        elif 65 <= ascii_value <= 90:  # 'A' to 'Z'
            has_upper = True
        elif 48 <= ascii_value <= 57:  # '0' to '9'
            has_digit = True
        elif (32 <= ascii_value <= 47) or (58 <= ascii_value <= 64) or \
             (91 <= ascii_value <= 96) or (123 <= ascii_value <= 126):  # Symbols
            has_symbol = True

    # Return True if all conditions are met
    return has_lower and has_upper and has_digit and has_symbol

def main():
   
    while True:
        password = input("Enter password to check:")
        if password_checker(password) == True:
            print("Good password\n")
            break
        else:
            print("Weak Password\n")

if __name__ == "__main__":
    main()


































import re

def password_checker(input):
    # Check if the length is between 8 and 20 characters
    if len(input) < 8 or len(input) > 20:
        return False


    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+\[\]{}|;:',.<>?/`~])[^\s]{8,20}$"

    if re.match(pattern, input):
        return True
    else:
        return False
    
def main():
    while True:
        

        password = input("Enter password to check:")
        if password_checker(password) == True:
            print("Good password\n")
            break
        else:
            print("Weak Password\n")

if __name__ == "__main__":
    main()
