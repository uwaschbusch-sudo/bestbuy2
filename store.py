class Store:
    """Ein Geschäft, das mehrere Produkte verwaltet."""

    def __init__(self, product_list=None):
        """Legt das Geschäft mit einer Produktliste an."""
        self.products = list(product_list) if product_list else []

    def add_product(self, product):
        """Fügt ein Produkt hinzu."""
        self.products.append(product)

    def remove_product(self, product):
        """Entfernt ein Produkt aus dem Geschäft."""
        if product not in self.products:
            raise ValueError("Das Produkt ist nicht im Geschäft.")
        self.products.remove(product)

    def get_total_quantity(self):
        """Gibt die Gesamtmenge aller Produkte zurück."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """Gibt alle aktiven Produkte zurück."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """Kauft die Produkte der Liste und gibt den Gesamtpreis zurück."""
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError("Das Produkt ist nicht im Geschäft.")
            total_price += product.buy(quantity)
        return total_price
