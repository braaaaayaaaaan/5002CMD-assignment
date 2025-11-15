from HashTable import HashTable

class BabyProduct:
    def __init__(self, product_id, name, category, price, quantity):
        """
        Represents a baby product with the following attributes:
        id, name, category, price, quantity
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"BabyProduct({self.name}, {self.category}, RM{self.price:.2f}, Quantity:{self.quantity})"

def get_baby_products():
    """Returns a list of predefined BabyProduct instances"""
    return [
        BabyProduct("P001", "Diapers", "Hygiene", 35.90, 100),
        BabyProduct("P002", "Milk Bottle", "Feeding", 19.50, 50),
        BabyProduct("P003", "Lotion", "Skincare", 12.80, 80),
        BabyProduct("P004", "Wet Wipes", "Hygiene", 8.90, 120),
        BabyProduct("P005", "Strollers", "Outdoor", 100.45, 10)
    ]

if __name__ == "__main__":
    # Create a hash table (storage) for the baby products
    product_storage = HashTable(10)

    # Insert the array of baby products into the hash table
    for product in get_baby_products():
        product_storage.insert(product.product_id, product)

    # Display the hash table of baby products
    product_storage.print_table()
