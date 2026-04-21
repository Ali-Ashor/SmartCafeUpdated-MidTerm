#File and Search
from menu_item import MenuItem

def save_menu(menu):
    with open("data/menu.txt", "w") as file:
        for item in menu:
            file.write(f"{item.name},{item.price},{item.category}\n")


def load_menu():
    menu = []
    try:
        with open("data/menu.txt", "r") as file:
            for line in file:
                name, price, category = line.strip().split(",")
                menu.append(MenuItem(name, float(price), category))
    except FileNotFoundError:
        print("Menu file not found!")
    return menu


def search_item(menu, name):
    for item in menu:
        if item.name.lower() == name.lower():
            item.display()
            return
    print("Item not found!")


def filter_by_category(menu, category):
    for item in menu:
        if item.category.lower() == category.lower():
            item.display()