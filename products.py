class Product:
    """Ein Produkt im Geschäft mit Name, Preis, Menge und Status."""

    def __init__(self, name, price, quantity):
        """Legt ein Produkt an und prüft die Werte."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Der Name darf nicht leer sein.")
        if price < 0:
            raise ValueError("Der Preis darf nicht negativ sein.")
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Gibt die Menge zurück."""
        return self.quantity

    def set_quantity(self, quantity):
        """Setzt die Menge und deaktiviert das Produkt bei 0."""
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Gibt zurück, ob das Produkt aktiv ist."""
        return self.active

    def activate(self):
        """Aktiviert das Produkt."""
        self.active = True

    def deactivate(self):
        """Deaktiviert das Produkt."""
        self.active = False

    def show(self):
        """Gibt das Produkt auf der Konsole aus."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """Kauft die Menge und gibt den Gesamtpreis zurück."""
        if not self.active:
            raise ValueError("Das Produkt ist nicht aktiv.")
        if quantity <= 0:
            raise ValueError("Die Kaufmenge muss größer als 0 sein.")
        if quantity > self.quantity:
            raise ValueError("Nicht genug Ware im Lager.")
        total_price = float(self.price * quantity)
        self.set_quantity(self.quantity - quantity)
        return total_price


def main():
    """Testet die Klasse Product."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
