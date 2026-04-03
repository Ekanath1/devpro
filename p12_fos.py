# this project is food management system
# from p8_login_with_food_order import FoodOrderingSystem

# food ordering system

class FoodOrderingSystem:
    def __init__(self):
        self.cart = []
        self.foods = [
            {"Burger": 120},
            {"Vegetable Pups": 50},
            {"Chinese Food": 100},
            {"Egg Pups": 50},
            {"Veg Pizza": 70},
            {"Chicken Pizza": 120}
        ]

    def display_menu(self):
        print("\n--- Menu ---")
        for item in self.foods:
            for food, price in item.items():
                print(f"{food} --> {price}")
        print("------------")


    def add_items(self):
        while True:
            itm = input("Which food would you like to add? ").title()
            found = False
            for food in self.foods:
                if itm in food:
                    self.cart.append(food)
                    print(f"{itm} added to cart.")
                    found = True
                    break
            if not found:
                print(f" {itm} is not available.")

            inp = input("Do you want to add more food? (yes/no): ").strip().lower()
            if inp == 'no':
                break

    def display_bill(self):
        cgst, sgst = 0, 0
        if not self.cart:
            print(" Your cart is empty.")
            return

        print("\n--- Bill ---")
        total_price = 0
        for item in self.cart:
            for food, price in item.items():
                print(f"{food}: ₹{price}")
                total_price += price

        if total_price >= 100:
            cgst = total_price*0.05
            sgst = total_price*0.05
            print('gst amount added ',cgst,sgst)

        print(f"Total Amount : ₹{total_price+cgst+sgst}")

        print("----- Thank you visit again -------")

    def delete_item(self):
        item1 = input("Enter the name of the item you want to delete from menu: ").title()
        for food in self.foods:
            if item1 in food:
                self.foods.remove(food)
                print(f" {item1} has been removed from the menu.")
                return
        print("Item not found in the menu.")

# Usage
food_ordering_system = FoodOrderingSystem()
while True:
    print("\n1. View Menu\n2. Add Items\n3. View Bill\n4. Delete Item From Menu\n5. Exit")
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        food_ordering_system.display_menu()
    elif choice == '2':
        food_ordering_system.add_items()
    elif choice == '3':
        food_ordering_system.display_bill()
    elif choice == '4':
        food_ordering_system.delete_item()
    elif choice == '5':
        break
    else:
        print("Invalid choice, please try again.")
