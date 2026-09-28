class Product:

    def __init__(self, name, price, quantity):
        if name == "":
            raise Exception("Name cannot be empty")

        if price < 0:
            raise Exception("Price cannot be negative")

        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.quantity = quantity

        if quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity must be positive")

        if quantity > self.quantity:
            raise Exception("Not enough products in stock")

        self.set_quantity(self.quantity - quantity)

        return self.price * quantity


class NonStockedProduct(Product):

    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self):
        print(f"{self.name}, Price: {self.price}, Non-stocked product")

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity must be positive")

        return self.price * quantity

class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception("Cannot buy more than the maximum quantity")

        return super().buy(quantity)

    def show(self):
        print( f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}")
