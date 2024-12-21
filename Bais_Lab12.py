def display_menu():
    menu = {
        "Burger": 120.00,
        "Pizza": 180.00,
        "Milktea": 90.00,
        "Pastil": 80.00,
        "Chicken": 50.00,
    }
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: ₱{price:.2f}")
    return menu

def get_order(menu):
    while True:
        choice = input("\nEnter the name of the item you'd like to order: ").strip()
        if choice in menu:
            print(f"You selected {choice} for ₱{menu[choice]:.2f}")
            return choice, menu[choice]
        else:
            print("Invalid choice. Please select an item from the menu.")

def process_payment(total):
    while True:
        try:
            cash = float(input(f"The total is ₱{total:.2f}. Enter cash amount: "))
            if cash >= total:
                change = cash - total
                print(f"Payment accepted. Your change is ₱{change:.2f}.")
                break
            else:
                print(f"Insufficient amount. You still owe ₱{total - cash:.2f}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def food_ordering_system():
    menu = display_menu()
    item, price = get_order(menu)
    process_payment(price)

# To execute the program, simply call the function below
food_ordering_system()
