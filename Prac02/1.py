#test
user_name = str(input("Please enter your name"))

name_file = open("name.txt", "w")
print(user_name, file = name_file)
name_file.close()