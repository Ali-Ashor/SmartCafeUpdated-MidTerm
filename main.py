# ==========================================
# SMART CAFE ORDERING SYSTEM (PYTHON)
# Advanced Version with Extra Features
# ==========================================

import os
import time
import random

MENU_FILE = "menu.txt"
ORDERS_FILE = "orders.txt"

# ==========================================
# MENU ITEM CLASS
# ==========================================

class MenuItem:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def display(self):
        print(f"{self.name} | Rs.{self.price} | {self.category} | Stock: {self.stock}")


# ==========================================
# PERSON CLASS (Inheritance)
# ==========================================

class Person:
    def __init__(self, name):
        self.name = name


# ==========================================
# CUSTOMER CLASS
# ==========================================

class Customer(Person):

    customer_counter = 1000

    def __init__(self, name):
        super().__init__(name)
        Customer.customer_counter += 1
        self.customer_id = Customer.customer_counter
        self.orders = []
        self.loyalty_points = 0

    def show_details(self):
        print("\nCustomer Details")
        print("----------------------")
        print(f"Name: {self.name}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Loyalty Points: {self.loyalty_points}")


# ==========================================
# STAFF CLASS
# ==========================================

class Staff(Person):

    def manage_menu(self):
        print("\nAdmin Menu Management")


# ==========================================
# ORDER CLASS
# ==========================================

class Order:

    TAX = 0.05

    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):

        if quantity > item.stock:
            raise Exception("Not enough stock available!")

        self.items.append((item, quantity))
        item.stock -= quantity

    def remove_item(self, item_name):

        for i in self.items:
            if i[0].name.lower() == item_name.lower():
                self.items.remove(i)
                print("Item removed successfully!")
                return

        print("Item not found!")

    def calculate_total(self):

        if len(self.items) == 0:
            raise Exception("Order is empty!")

        subtotal = 0

        for item, qty in self.items:
            subtotal += item.price * qty

        tax = subtotal * Order.TAX
        total = subtotal + tax

        return subtotal, tax, total

    def display_receipt(self, customer):

        subtotal, tax, total = self.calculate_total()

        print("\n========== SMART CAFE ==========")

        for item, qty in self.items:
            print(f"{item.name} x{qty} = Rs.{item.price * qty}")

        print("--------------------------------")
        print(f"Subtotal: Rs.{subtotal}")
        print(f"Tax (5%): Rs.{tax}")

        # EXTRA FEATURE 1
        # Student Discount

        discount = 0

        student = input("Are you a student? (y/n): ")

        if student.lower() == 'y':
            discount = total * 0.10
            total -= discount
            print(f"Student Discount: -Rs.{discount}")

        print("--------------------------------")
        print(f"Final Total: Rs.{total}")

        # EXTRA FEATURE 2
        # Loyalty Points

        earned_points = int(total / 100)
        customer.loyalty_points += earned_points

        print(f"Earned Loyalty Points: {earned_points}")

        print("================================")

        self.save_receipt(customer, subtotal, tax, discount, total)

    def save_receipt(self, customer, subtotal, tax, discount, total):

        with open(ORDERS_FILE, "a") as file:

            file.write("\n========== SMART CAFE ==========\n")
            file.write(f"Customer: {customer.name}\n")
            file.write(f"Customer ID: {customer.customer_id}\n")

            for item, qty in self.items:
                file.write(f"{item.name} x{qty} = Rs.{item.price * qty}\n")

            file.write(f"\nSubtotal: Rs.{subtotal}\n")
            file.write(f"Tax: Rs.{tax}\n")
            file.write(f"Discount: Rs.{discount}\n")
            file.write(f"Total: Rs.{total}\n")
            file.write("================================\n")


# ==========================================
# FILE HANDLING
# ==========================================

menu = []

def load_menu():

    if not os.path.exists(MENU_FILE):

        default_items = [
            "Burger,500,Fast Food,10",
            "Pizza,1200,Fast Food,5",
            "Coffee,300,Drinks,20",
            "Ice Cream,250,Desserts,15"
        ]

        with open(MENU_FILE, "w") as file:
            for item in default_items:
                file.write(item + "\n")

    with open(MENU_FILE, "r") as file:

        for line in file:

            name, price, category, stock = line.strip().split(",")

            menu.append(
                MenuItem(
                    name,
                    float(price),
                    category,
                    int(stock)
                )
            )


def save_menu():

    with open(MENU_FILE, "w") as file:

        for item in menu:

            file.write(
                f"{item.name},{item.price},{item.category},{item.stock}\n"
            )


# ==========================================
# DISPLAY MENU
# ==========================================

def display_menu():

    print("\n========== MENU ==========")

    for i, item in enumerate(menu):
        print(f"{i+1}. ", end="")
        item.display()


# ==========================================
# SEARCH FEATURE
# ==========================================

def search_item():

    keyword = input("Enter item name: ").lower()

    found = False

    for item in menu:

        if keyword in item.name.lower():
            item.display()
            found = True

    if not found:
        print("Item not found!")


# ==========================================
# FILTER FEATURE
# ==========================================

def filter_category():

    category = input("Enter category: ").lower()

    found = False

    for item in menu:

        if category == item.category.lower():
            item.display()
            found = True

    if not found:
        print("No items in this category!")


# ==========================================
# ADMIN LOGIN
# ==========================================

def admin_panel():

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":

        while True:

            print("\n===== ADMIN PANEL =====")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. View Menu")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == '1':

                name = input("Item name: ")
                price = float(input("Price: "))
                category = input("Category: ")
                stock = int(input("Stock: "))

                menu.append(
                    MenuItem(name, price, category, stock)
                )

                save_menu()

                print("Item added successfully!")

            elif choice == '2':

                name = input("Enter item name to remove: ")

                for item in menu:

                    if item.name.lower() == name.lower():
                        menu.remove(item)
                        save_menu()
                        print("Item removed!")
                        break

            elif choice == '3':
                display_menu()

            elif choice == '4':
                break

            else:
                print("Invalid choice!")

    else:
        print("Invalid Login!")


# ==========================================
# MAIN PROGRAM
# ==========================================

def loading():

    print("Loading Smart Cafe", end="")

    for i in range(5):
        print(".", end="")
        time.sleep(0.5)

    print()


load_menu()

loading()

print("\n========== SMART CAFE SYSTEM ==========")

customer_name = input("Enter your name: ")

customer = Customer(customer_name)

order = Order()

while True:

    print("\n========== MAIN MENU ==========")
    print("1. View Menu")
    print("2. Search Item")
    print("3. Filter Category")
    print("4. Add Item to Order")
    print("5. Remove Item from Order")
    print("6. Checkout")
    print("7. Customer Details")
    print("8. Admin Panel")
    print("9. Exit")

    choice = input("Enter choice: ")

    try:

        if choice == '1':

            display_menu()

        elif choice == '2':

            search_item()

        elif choice == '3':

            filter_category()

        elif choice == '4':

            display_menu()

            item_no = int(input("Enter item number: ")) - 1
            quantity = int(input("Enter quantity: "))

            order.add_item(menu[item_no], quantity)

            print("Item added successfully!")

        elif choice == '5':

            item_name = input("Enter item name to remove: ")

            order.remove_item(item_name)

        elif choice == '6':

            order.display_receipt(customer)

        elif choice == '7':

            customer.show_details()

        elif choice == '8':

            admin_panel()

        elif choice == '9':

            print("Thank You For Visiting Smart Cafe ")
            break

        else:
            print("Invalid Choice!")

    except Exception as e:
        print("Error:", e)
