import random

def main():
    number_of_quickpicks = int(input("How many quick picks would you like to generate?: "))
    for num in range(0, number_of_quickpicks):
        random_numbers = []
        for i in range(0,6):
            random_number = random.randint(1,45)
            while random_number in random_numbers:
                random_number = random.randint(1, 45)
            random_numbers.append(random_number)
        print("{} {} {} {} {} {}".format(random_numbers[0],random_numbers[1],random_numbers[2],random_numbers[3],random_numbers[4],random_numbers[5]))


main()