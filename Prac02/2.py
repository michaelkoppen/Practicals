#commit
name_file = open("name.txt", "r")
user_name = name_file.read()
print("Your name is", user_name)
name_file.close()