class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total = 0

        for product in self.products:
            total += product.quantity

        return total

    def get_all_products(self):
        active_products = []

        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list):
        quantities = {}

        for product, quantity in shopping_list:
            if product in quantities:
                quantities[product] += quantity
            else:
                quantities[product] = quantity

        total_price = 0

        for product, quantity in quantities.items():
            total_price += product.buy(quantity)

        return total_price

    def __contains__(self, product):
        return product in self.products

    def __add__(self, other):
        if not isinstance(other, Store):
            return NotImplemented

        return Store(self.products + other.products)
