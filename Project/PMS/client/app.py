"""
This script provides a command-line interface for managing products using a 'repo_api' module.
It allows users to add, list, retrieve, update, delete products, view total stock,
and scrape products. It also sets up basic logging for error handling.
"""

import repo_api as repo
import logging
from pathlib import Path

LOGS_DIR = Path(__file__).parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOGS_DIR / 'client.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# Note: The second basicConfig call will overwrite the first one if it's not handled carefully.
# Typically, basicConfig should only be called once. If you intend to log to both file and console,
# you should configure handlers explicitly. For simplicity, if the intent is only file logging,
# the second basicConfig call can be removed. If the intent is console logging for INFO level
# in addition to file logging, then a handler should be added to the root logger.
# For this example, assuming the file logging is the primary intent, and the second
# basicConfig might be redundant or an oversight.
# For demonstration, I'll keep it as is, but note the potential for overwriting.
logging.basicConfig(level=logging.INFO)

def menu():
    """
    Displays the product management menu options to the user and
    prompts for a choice.

    Returns:
        int: The integer choice entered by the user.
    """
    print("""
    Product Management Menu:
    1 - Add Product
    2 - List Products
    3 - Get by ID
    4 - Update Product
    5 - Delete Product
    6 - Show Total Stock
    7 - Scrape Products
    8 - Exit
    """)
    choice = int(input("Enter choice: "))
    return choice

def run():
    """
    Runs the main product management application loop.
    It continuously displays the menu, takes user input, and performs
    corresponding product operations using the 'repo_api' module until
    the user chooses to exit. Errors during operations are logged.
    """
    choice = menu()
    while choice != 8:
        try:
            if choice == 1:
                name = input("Name: ")
                qty = int(input("Quantity: "))
                price = float(input("Price: "))
                p = repo.create_product({"name": name, "qty": qty, "price": price})
                print("Added:", p)
            elif choice == 2:
                prods = repo.read_all()
                for p in prods:
                    print(p)
            elif choice == 3:
                pid = int(input("ID: "))
                print(repo.read_by_id(pid))
            elif choice == 4:
                pid = int(input("ID: "))
                name = input("Name: ")
                qty = int(input("Quantity: "))
                price = float(input("Price: "))
                print(repo.update({"id": pid, "name": name, "qty": qty, "price": price}))
            elif choice == 5:
                pid = int(input("ID: "))
                print(repo.delete_by_id(pid))
            elif choice == 6:
                print(repo.get_total_stock())
            elif choice == 7:
                print(repo.scrape_products())
        except Exception as e:
            logging.error(f"Error: {e}")
        choice = menu()

if __name__ == "__main__":
    run()