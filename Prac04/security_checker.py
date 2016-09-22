def main():
    usernames = ["jimbo", "giltson98", "derekf", "WhatSup", "NicolEye",
    "swei45", "BaseInterpreterInterface", "BaseStdIn", "Command", "ExecState",
    "InteractiveConsole", "InterpreterInterface", "StartServer", "bob"]

    username = input("Enter your username: ")
    while username not in usernames:
        print("Access denied")
        username = str(input("Enter your username: "))
    print("Access granted")

main()