from person import Person

class Customer(Person):
    def __init__(self, name, customer_id):
        super().__init__(name)
        self.customer_id = customer_id
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)