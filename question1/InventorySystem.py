from HashTable import HashTable
from BabyProduct import BabyProduct, get_baby_products


class InventorySystem:
    def __init__(self):
        self.storage = HashTable(10)
        self._load_products()

    def _load_products(self):
        """Load array of baby products"""
        for product in get_baby_products():
            # Insert each instance of baby product into hash table
            self.storage.insert(product.product_id, product)

    """Inventory System's Functionalities"""

    def insert_product(self):
        """Insert new product into the system"""
        print("\n=== Insert New Product ===\n")

        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")

        try:
            price = float(input("Enter Price (RM): "))
            qty = int(input("Enter Quantity: "))
        except ValueError:
            print("Invalid numeric input. Product NOT inserted.\n")
            return

        # Create a new instance for the baby product
        new_product = BabyProduct(pid, name, category, price, qty)

        # Insert the baby product into the hash table
        self.storage.insert(pid, new_product)
        print("\nSuccessfully Inserted Product!\n")

    def search_product(self):
        """Search for Product based on ID"""
        print("\n=== Search Product ===\n")

        # Search by product ID
        pid = input("Enter Product ID: ")
        result = self.storage.search(pid)

        # Check if the product exists
        if result:
            print(f"\nFound Matching Product ID: {pid}\n")
            print(result)
        else:
            print("\nFailed to Retrieve Matching Product ID.\n")

    def edit_product(self):
        """Edit product based on ID"""
        print("\n=== Edit Product ===\n")

        # Edit producy by identifying the ID
        pid = input("Enter Product ID: ")

        # First, search for product
        product = self.storage.search(pid)

        # If product does not exist, then return
        if not product:
            print("\nFailed to Retrieve Matching Product ID.\n")
            return

        print("Reminder: Leaving blank fields keep existing data")

        new_name = input(f"New Name ({product.name}): ") or product.name
        new_category = input(f"New Category ({product.category}): ") or product.category

        new_price_input = input(f"New Price ({product.price}): ")
        new_qty_input = input(f"New Quantity ({product.quantity}): ")

        try:
            new_price = float(new_price_input) if new_price_input else product.price
            new_qty = int(new_qty_input) if new_qty_input else product.quantity
        except ValueError:
            print("Invalid input. No changes made.\n")
            return

        # Create another instance to store updated product
        updated_product = BabyProduct(pid, new_name, new_category, new_price, new_qty)

        # Edit the product
        self.storage.edit(pid, updated_product)
        print("\nSuccessfully Updated Product!\n")

    def delete_product(self):
        """Delete product by ID"""
        print("\n=== Delete Product ===\n")

        # Delete by ID
        pid = input("Enter Product ID: ")

        deleted = self.storage.delete(pid)

        if deleted:
            print("\nSuccessfully Deleted Product!\n")
        else:
            print("\nFailed to Retrieve Matching Product ID.\n")

    def display_hash_table(self):
        """Display Hash Table"""
        print("\n=== Hash Table Contents ===")
        self.storage.print_table()
        print()


    """Loop the CLI"""

    def _display_menu(self):
        """Display the main menu"""

        # Display the menu design
        print("=" * 30)
        print("  BABY SHOP INVENTORY SYSTEM ")
        print("=" * 30)
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Display Hash Table")
        print("0. Exit")
        print("=" * 30)


    def _handle_choice(self, choice):
        """Handle user menu choice"""
        menu_actions = {
            "1": self.insert_product,
            "2": self.search_product,
            "3": self.edit_product,
            "4": self.delete_product,
            "5": self.display_hash_table,
        }

        if choice in menu_actions:
            menu_actions[choice]()
        elif choice == "0":
            print("Exiting system...")
            return False
        else:
            print("Invalid choice. Please try again.\n")

        return True

    def run(self):
        # Handles looping of menu
        terminate_menu = False

        while terminate_menu != True:
            self._display_menu()
            choice = input("\nEnter your choice: ")

            if not self._handle_choice(choice):
                terminate_menu = True
                break


if __name__ == "__main__":
    system = InventorySystem()
    system.run()