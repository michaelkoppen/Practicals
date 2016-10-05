from Prac07.GuitarClass import Guitar

print("My guitars!")
guitars = []

name = str(input("Name: "))
guitar_number_in_list = 0
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print("{} added.".format(guitars[guitar_number_in_list]))
    guitar_number_in_list += 1
    name = str(input("Name: "))

guitar_number = 0
print("These are my guitars:")
for guitar in guitars:
    if guitar.is_vintage():
        vintage_string = "(Vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(guitar_number + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
    guitar_number += 1
