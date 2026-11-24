import products
import store


def show_menu():
    """Zeigt das Menü an."""
    print("\n   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store_obj):
    """Listet alle aktiven Produkte nummeriert auf."""
    print("------")
    for index, product in enumerate(store_obj.get_all_products(), start=1):
        print(f"{index}. ", end="")
        product.show()
    print("------")


def show_total(store_obj):
    """Zeigt die Gesamtmenge im Geschäft an."""
    print(f"Total of {store_obj.get_total_quantity()} items in store")


def read_positive_int(text):
    """Wandelt Text in eine positive ganze Zahl um, sonst None."""
    if text.isdigit() and int(text) > 0:
        return int(text)
    return None


def make_order(store_obj):
    """Nimmt Bestellungen entgegen und führt sie aus."""
    active_products = store_obj.get_all_products()
    if not active_products:
        print("No products available.")
        return
    list_products(store_obj)
    print("When you want to finish the order, enter an empty text.")
    shopping_list = []
    requested = {}
    while True:
        number_text = input("Which product # do you want? ").strip()
        if number_text == "":
            break
        number = read_positive_int(number_text)
        if number is None or number > len(active_products):
            print("Invalid product number.")
            continue
        amount = read_positive_int(input("What amount do you want? ").strip())
        if amount is None:
            print("Invalid amount.")
            continue
        product = active_products[number - 1]
        if requested.get(product, 0) + amount > product.get_quantity():
            print("Not enough items in stock.")
            continue
        requested[product] = requested.get(product, 0) + amount
        shopping_list.append((product, amount))
        print("Product added to list!")
    if not shopping_list:
        print("Nothing ordered.")
        return
    try:
        total_price = store_obj.order(shopping_list)
        print(f"Order made! Total payment: ${total_price}")
    except ValueError as error:
        print(f"Order failed: {error}")


def start(store_obj):
    """Zeigt das Menü und führt die Auswahl aus."""
    while True:
        show_menu()
        choice = input("Please choose a number: ").strip()
        if choice == "4":
            break
        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            show_total(store_obj)
        elif choice == "3":
            make_order(store_obj)
        else:
            print("Invalid choice, please enter 1 to 4.")


def main():
    """Legt das Inventar an und startet die Benutzeroberfläche."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
