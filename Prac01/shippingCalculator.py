#commit
number_of_items = int(input("Enter number of items"))
while number_of_items < 0:
    number_of_items = int(input("Enter number of items greater than 0"))
item_list = []

for i in range(0, number_of_items, 1):
    print("Enter the price of item", i)
    price_of_items = float(input())
    item_list.append(price_of_items)

print("Number of items:", number_of_items)

for i in range(0, number_of_items, 1):
    print("Price of item:", item_list[i])


total_cost = sum(item_list)
if total_cost > 100:
    total_cost -= total_cost * 10 / 100

print("Total price for", number_of_items, "is ", total_cost)