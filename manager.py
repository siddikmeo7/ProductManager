import argparse

class ProductManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.products = self.load_products()

    def load_products(self):
        """Load products from file."""
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                products = []
                for line in lines:
                    name, price = line.strip().split(' — ')
                    products.append({'name': name, 'price': int(price)})
                return products
        except FileNotFoundError:
            return []

    def save_products(self):
        """Save products to file."""
        with open(self.file_name, 'w', encoding='utf-8') as file:
            for product in self.products:
                file.write(f"{product['name']} — {product['price']}\n")

    def add_product(self, name, price):
        """Add a new product."""
        self.products.append({'name': name, 'price': int(price)})
        self.save_products()
        print(f"Product '{name}' added successfully.")

    def update_product(self, name, new_price):
        """Update an existing product."""
        for product in self.products:
            if product['name'] == name:
                product['price'] = int(new_price)
                self.save_products()
                print(f"Product '{name}' updated successfully.")
                return
        print(f"Product '{name}' not found.")

    def delete_product(self, name):
        """Delete a product by name."""
        self.products = [product for product in self.products if product['name'] != name]
        self.save_products()
        print(f"Product '{name}' deleted successfully.")

    def calculate_total(self):
        """Calculate the total sum of all products."""
        total = sum(product['price'] for product in self.products)
        print(f"Total sum of all products: {total}")

def main():
    parser = argparse.ArgumentParser(description="Product Manager CLI")
    parser.add_argument("file_name", help="Name of the file to manage")
    parser.add_argument("action", help="Action to perform: add, update, delete, sum")
    parser.add_argument("--name", help="Name of the product")
    parser.add_argument("--price", type=int, help="Price of the product (for add or update)")
    args = parser.parse_args()

    manager = ProductManager(args.file_name)

    if args.action == "add":
        if args.name and args.price is not None:
            manager.add_product(args.name, args.price)
        else:
            print("Please provide --name and --price for the product.")
    elif args.action == "update":
        if args.name and args.price is not None:
            manager.update_product(args.name, args.price)
        else:
            print("Please provide --name and --price to update the product.")
    elif args.action == "delete":
        if args.name:
            manager.delete_product(args.name)
        else:
            print("Please provide --name to delete the product.")
    elif args.action == "sum":
        manager.calculate_total()
    else:
        print("Invalid action. Available actions: add, update, delete, sum")

if __name__ == "__main__":
    main()
