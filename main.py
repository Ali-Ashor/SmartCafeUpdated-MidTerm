from menu_item import MenuItem
from order import Order
from customer import Customer
from staff import Staff
from utils import save_menu, load_menu, search_item, filter_by_category


def print_bill(order):
    try:
        subtotal, tax, total = order.calculate_total()

        print("\n------ Smart Cafe ------")
        print("Item\tQty\tPrice")

        for i in range(len(order.items)):
            item = order.items[i]
            qty = order.quantity[i]
            print(f"{item.name}\t{qty}\t{item.price * qty}")

        print("------------------------")
        print(f"Subtotal: {subtotal}")
        print(f"Tax (5%): {tax}")
        print(f"Total: {total}")
        print("------------------------")

    except Exception as e:
        print(e)


def main():
    # Load or create menu
    menu = load_menu()
    if not menu:
        menu = [
            MenuItem("Coffee", 200, "Drink"),
            MenuItem("Burger", 500, "FastFood"),
            MenuItem("Cake", 300, "Dessert")
        ]

    customer = Customer("Ali", 101)
    order = Order()

    while True:
        print("\n1. View Menu\n2. Add Item\n3. Remove Item\n4. Search\n5. Filter\n6. Checkout\n7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            for item in menu:
                item.display()

        elif choice == "2":
            name = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            found = False
            for item in menu:
                if item.name.lower() == name.lower():
                    order.add_item(item, qty)
                    found = True
            if not found:
                print("Item not found!")

        elif choice == "3":
            name = input("Enter item to remove: ")
            order.remove_item(name)

        elif choice == "4":
            name = input("Search item: ")
            search_item(menu, name)

        elif choice == "5":
            cat = input("Enter category: ")
            filter_by_category(menu, cat)

        elif choice == "6":
            print_bill(order)
            customer.place_order(order)
            save_menu(menu)

        elif choice == "7":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()