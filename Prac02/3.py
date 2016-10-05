#commit
 = open("numbers.txt", "r")
number1 = int(number_file.readline())
number2 = int(number_file.readline())
print(number1 + number2)
number_file.close()