#commit
guitar_file = open("guitars.txt", "r")
for line in guitar_file:
    guitar, year, price = line.split(",")
print("Guitar: {}, Year: {}, Price: ${}".format(guitar, year, price))
