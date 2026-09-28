from products import Product
from store import Store

def start(store):
    while True:
        print("\nStore Menu \n---------- \n1. List all products in store \n2. Show total amount in store \n3. Make an order \n4. Quit")

        choice = input("\nPlease choose a number: ")

        if choice == "1":
            products = store.get_all_products()
            print("------")

            for product in products:
                product.show()

            print("------")

        elif choice == "2":
            print(f"Total quantity in store: {store.get_total_quantity()}")

        elif choice == "3":
            all_products = store.get_all_products()
            print("------")

            for i, product in enumerate(all_products, start=1):
                print(f"{i}. ", end="")
                product.show()

            print("------")

            print("When you want to finish order, enter empty text.")

            shopping_list = []

            while True:
                product_number = input("Which product # do you want? ")

                if product_number == "":
                    break

                try:
                    product_number = int(product_number)

                    if product_number < 1 or product_number > len(all_products):
                        raise Exception()

                    quantity = int(input("What amount do you want? "))
                    shopping_list.append((all_products[product_number - 1], quantity))

                    print("Product added to list!\n")

                except Exception:
                    print("Error adding product!")

            try:
                total_price = store.order(shopping_list)

                print("********")
                print(f"Order made! Total payment: ${total_price}")

            except Exception as e:
                print(f"Error while making order! {e}")

        elif choice == "4":
            break

        else:
            print("Invalid choice")

def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)]

    best_buy = Store(product_list)

    start(best_buy)

if __name__ == "__main__":
    main()
