class Product:

    def __init__(self, name, price, quantity):
        if name == "":
            raise Exception("Name cannot be empty")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None
        self.active = True

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise Exception("Price cannot be negative")

        self._price = price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self._quantity = quantity

        if quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def __str__(self):
        text = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

        if self.promotion is not None:
            text += f", Promotion: {self.promotion.name}"

        return text

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity must be positive")

        if quantity > self.quantity:
            raise Exception("Not enough products in stock")

        total_price = self.calculate_price(quantity)

        self.quantity = self.quantity - quantity

        return total_price

    def calculate_price(self, quantity):
        if self.promotion is not None:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.price < other.price

    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.price > other.price


class NonStockedProduct(Product):

    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def __str__(self):
        text = f"{self.name}, Price: {self.price}, Non-stocked product"

        if self.promotion is not None:
            text += f", Promotion: {self.promotion.name}"

        return text

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity must be positive")

        return self.calculate_price(quantity)


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def __str__(self):
        text = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"

        if self.promotion is not None:
            text += f", Promotion: {self.promotion.name}"

        return text

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception("Cannot buy more than the maximum quantity")

        return super().buy(quantity)
