class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        print(f"{self.name} - Rs.{self.price} ({self.category})")