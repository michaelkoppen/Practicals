
#test
def main():
    LOWER = int(33)
    UPPER = int(127)
    user_input_character = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(user_input_character, ord(user_input_character)))

    user_number = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(user_number ,chr(user_number)))

    for i in range(LOWER, UPPER+1):
        print("{:3}  {}".format(i, chr(i)))

def get_number(LOWER, UPPER):
    user_input_number = int(input("Enter a number between 33 and 127: "))
    while LOWER > user_input_number or UPPER < user_input_number:
        user_input_number = int(input("Please enter a number between 33 and 127: "))
    return user_input_number


main()