#commit
def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            temperature_in_fahrenheit = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(temperature_in_fahrenheit))
        elif choice == "F":
            # TODO: Write this section so the program converts F to C and displays the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            fahrenheit = float(input("Farenheit: "))
            temperature_in_celsius = fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(temperature_in_celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()