
Books = {'Python':500, 'Sql':450, 'Java':600,'Js':550,'Hadoop':600,'Typescript':600}

for book, value in Books.items():
    print(f"{book} price is {value}")

shopping_cart = []
total_price = 0
discount_percentage = 10

while True:
    selected_book = input("Enter which book you want or type done to exit ..").capitalize()

    if selected_book == 'Done':
        break

    if selected_book in Books:
        shopping_cart.append(selected_book)
        total_price += Books[selected_book]
        print(f"{selected_book} is added to cart.")
    else:
        print(f"{selected_book} is not available")


if len(shopping_cart) >= 5:
    discount_percentage = 20
    discount = (total_price*discount_percentage)/100
    final_cost = total_price - discount
    print(f"your actual order price is {total_price}")
    print(f"final price after discount {final_cost}")

elif 2 < len(shopping_cart) < 5:
    discount = (total_price * discount_percentage) / 100
    final_cost = total_price - discount
    print(f"your actual order price is {total_price}")
    print(f"final price after discount {final_cost}")
else:
    print(f"total cost of your order is {total_price}")

print('@@@@@@ visit again @@@@@@')
