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
        self.promotion = None
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
        text = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

        if self.promotion is not None:
            text += f", Promotion: {self.promotion.name}"

        print(text)

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity must be positive")

        if quantity > self.quantity:
            raise Exception("Not enough products in stock")

        total_price = self.get_price(quantity)

        self.set_quantity(self.quantity - quantity)

        return total_price

    def get_price(self, quantity):
        if self.promotion is not None:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion


class NonStockedProduct(Product):

    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self):
        text = f"{self.name}, Price: {self.price}, Non-stocked product"

        if self.promotion is not None:
            text += f", Promotion: {self.promotion.name}"

        print(text)

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity must be positive")

        return self.get_price(quantity)


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        text = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"

        if self.promotion is not None:
            text += f", Promotion: {self.promotion.name}"

        print(text)

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception("Cannot buy more than the maximum quantity")

        return super().buy(quantity)
