class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Dodat proizvod: {product.name}")

    # --- OVDE DODAJ NOVI METOD ---
    def remove_product(self, product_name):
        """Uklanja proizvod iz liste na osnovu imena."""
        original_count = len(self.products)
        # Filtriramo listu tako da zadržimo sve OSIM onog koji brišemo
        self.products = [p for p in self.products if p.name.lower() != product_name.lower()]
        
        if len(self.products) < original_count:
            print(f"Proizvod '{product_name}' je uspešno uklonjen.")
        else:
            print(f"Proizvod '{product_name}' nije pronađen.")

    def display_all_products(self):
        # ... ostatak koda ...