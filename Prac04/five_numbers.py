def main():
    numbers = []
    for num in range(1, 6):
        number = int(input("Number: "))
        numbers.append(number)
    print("The first number is: {}".format(numbers[0]))
    print("The last number is: {}".format(numbers[4]))
    print("The smallest number is: {}".format(min(numbers)))
    print("The largest number is: {}".format(max(numbers)))
    average = sum(numbers)/len(numbers)
    print("The average of the numbers is {}".format(average))
main()