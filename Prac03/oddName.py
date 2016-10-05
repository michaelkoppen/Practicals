"""
Michael
"""
#commit
def main():
    user_name = get_name()
    count = 3
    print_loop(count, user_name)


def print_loop(count, user_name):
    for char in list(user_name)[::count]:
        print(char, end=" ")



def get_name():
    user_name = input("Enter your name: ")
    while user_name == "":
        user_name = input("Make sure field is not blank: ")
    return user_name

main()














