
inventory = {}

while True:
    item = input("Enter item or type done to exit ").capitalize()

    if item == 'Done':
        break

    qty = input(f"Enter quantity {item} ").capitalize()
    try:
        if not qty.isdigit() :
            print('quantity should be valid ')
            continue
    except ValueError:
        print("valid quantity should be integer ")


    if item in inventory:
        inventory[item] += int(qty)
    else:
        inventory[item] = int(qty)

for item, value in inventory.items():
    print(f"item {item} and   quantity {value}")

