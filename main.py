MENU = {
    1: ("Croissant", 10.00),
    2: ("Chocolate Muffin", 2.50),
    3: ("Bread", 2.00),
}
DISCOUNT_THRESHOLD = 10.00
DISCOUNT_RATE = 0.10
LINE = "=" * 31


def read_int(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError:
        return None


def read_float(prompt):
    try:
        return float(input(prompt).strip())
    except ValueError:
        return None


def show_main_menu():
    print(LINE)
    print("    WELCOME TO OUR BAKERY")
    print(LINE)
    print("1. Order Items")
    print("2. View Total")
    print("3. Checkout")
    print("4. Exit")
    print(LINE)


def show_bakery_menu():
    print("========BAKERY MENU==========")
    for number, (name, price) in MENU.items():
        print(f"{number}. {name:<18}${price:.2f}")
    print(f"{len(MENU) + 1}. Back to Main Menu")
    print(LINE)


def order_items(subtotal):
    show_bakery_menu()
    choice = read_int("Select an item: ")

    if choice in MENU:
        name, price = MENU[choice]
        subtotal += price
        print(f"{name} added successfully!")
    elif choice == len(MENU) + 1:
        return subtotal
    else:
        print("Invalid item selection!")
        print("Subtotal remains unchanged.")

    print(f"Current Subtotal: ${subtotal:.2f}")
    return subtotal


def view_total(subtotal):
    print("=========YOUR ORDER==========")
    if subtotal == 0:
        print("Your order is empty")
    else:
        print(f"Current Subtotal: ${subtotal:.2f}")


def checkout(subtotal):
    print("===========CHECKOUT===========")

    if subtotal == 0:
        print("Your order is empty.")
        print("Please order something first.")
        return subtotal

    discount = subtotal * DISCOUNT_RATE if subtotal >= DISCOUNT_THRESHOLD else 0.0
    final_total = subtotal - discount

    print(f"{'Subtotal:':<24}${subtotal:.2f}")
    if discount > 0:
        print(f"{'Discount (10%):':<24}${discount:.2f}")
    else:
        print(f"{'Discount':<24}${discount:.2f}")
    print("-" * 31)
    print(f"{'Final Total:':<24}${final_total:.2f}")

    cash = read_float("Enter cash received ($): ")
    if cash is None or cash < 0:
        print("Invalid amount!")
        return subtotal

    print("===========PAYMENT============")
    if cash >= final_total:
        print(f"{'Final Total':<24}${final_total:.2f}")
        print(f"{'Cash Received':<24}${cash:.2f}")
        print(f"{'Change':<24}${cash - final_total:.2f}")
        return 0.0
    else:
        print("Insufficient Payment!")
        print(f"You need ${final_total - cash:.2f} more.")
        return subtotal


def main():
    subtotal = 0.0

    while True:
        show_main_menu()
        option = read_int("Select an option: ")
        print()

        if option == 1:
            subtotal = order_items(subtotal)
        elif option == 2:
            view_total(subtotal)
        elif option == 3:
            subtotal = checkout(subtotal)
        elif option == 4:
            print("Thank you for supporting our Bakery!")
            print("Have a greate day!")
            break
        else:
            print("Invalid option! Please try again.")

        print()


if __name__ == "__main__":
    main()