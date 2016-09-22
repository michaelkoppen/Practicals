
user_dictionary = {}
print("Enter a string that will be converted to a list")
string_for_list = input(">>> ")
user_list = string_for_list.split()
print("Text: {}".format(string_for_list))




for word in user_list:
    print(word)
    if word in user_dictionary:
        user_dictionary[word] += 1

    else:
        user_dictionary[word] = 1


print(user_dictionary)


