class ProductManager:
 from product import Product
from cart import Cart # Dodaj ovaj import

# ... tvoj postojeći ProductManager ostaje isti ...

if __name__ == "__main__":
    # Inicijalizacija managera i proizvoda
    manager = ProductManager()
    p1 = Product("Laptop", 75000, 5)
    p2 = Product("Miš", 3200, 10)
    p3 = Product("Tastatura", 4500, 8)
    
    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # NOVO: Kreiranje instance Cart
    moja_korpa = Cart()

    # Dodavanje proizvoda u korpu (simulacija kupovine)
    moja_korpa.add_to_cart(p1, 1) # 1 Laptop
    moja_korpa.add_to_cart(p2, 2) # 2 Miša
    moja_korpa.add_to_cart(p3, 1) # 1 Tastatura

    # Prikaz korpe i naplata
    moja_korpa.display_cart()
    print(f"Ukupan iznos za naplatu: {moja_korpa.calculate_total():.2f} RSD")
    
    # Provera preostalih zaliha nakon kupovine
    manager.display_all_products()
if __name__ == "__main__":
    manager = ProductManager()
    p1 = Product("Felna", 12000, 4) # Promijenjeno
    p2 = Product("Ulje", 1500, 10)   # Promijenjeno
    
    manager.add_product(p1)
    manager.add_product(p2)
    
    # Ovdje su obrisane linije za prikaz inventara