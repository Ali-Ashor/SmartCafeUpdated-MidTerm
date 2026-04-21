class Order:
    def __init__(self):
        self.items = []
        self.quantity = []

    def add_item(self, item, qty):
        self.items.append(item)
        self.quantity.append(qty)

    def remove_item(self, item_name):
        for i in range(len(self.items)):
            if self.items[i].name.lower() == item_name.lower():
                self.items.pop(i)
                self.quantity.pop(i)
                print("Item removed!")
                return
        print("Item not found!")

    def calculate_total(self):
        if not self.items:
            raise Exception("Order is empty!")

        subtotal = 0
        for i in range(len(self.items)):
            subtotal += self.items[i].price * self.quantity[i]

        tax = subtotal * 0.05
        total = subtotal + tax
        return subtotal, tax, total

    def display_order(self):
        print("\nYour Order:")
        for i in range(len(self.items)):
            print(f"{self.items[i].name} x{self.quantity[i]}")