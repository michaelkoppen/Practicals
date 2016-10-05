try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator
except ValueError:
 print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
 print("Cannot divide by zero!")
print("Finished.")

#1. When will a ValueError occur?
#A. When a non integer value is entered for either the numerator or denominator.

#2. When will a ZeroDivisionError occur?
#A. When 0 is entered as the denominator.

#3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#A. Yes you could add error checking as a while statement that will ask the user to enter a number other than 0.

#commit