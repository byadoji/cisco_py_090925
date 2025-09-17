"""
This Flask application provides a RESTful API for managing products.
It integrates with a product repository (product_repo), a stock calculation module,
a web scraper, and an email sending utility.

The API supports the following operations:
- GET /products: Retrieve all products.
- GET /products/<prod_id>: Retrieve a single product by ID.
- POST /products: Create a new product.
- PUT /products/<prod_id>: Update an existing product.
- DELETE /products/<prod_id>: Delete a product.
- GET /stock/total: Get the total stock quantity of all products.
- GET /products/scrape: Scrape products from an external source.

Logging is configured to INFO level.
"""

from flask import Flask, request, jsonify
from datetime import datetime
import logging
from mail_send import send_gmail
import product_repo as repo
import stock_calc
import scraper

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
repo.product_table_create()


@app.route("/products", methods=['GET'])
def get_all():
    """
    Retrieves all products from the repository.

    Returns:
        jsonify: A JSON array of all product objects.
    """
    products = repo.read_all_products()
    return jsonify([p.__dict__ for p in products])


@app.route("/products/<int:prod_id>", methods=['GET'])
def get_by_id(prod_id):
    """
    Retrieves a single product by its ID.

    Args:
        prod_id (int): The ID of the product to retrieve.

    Returns:
        jsonify: A JSON object of the product if found, or an error message
                 with a 404 status if not found.
    """
    product = repo.read_product_by_id(prod_id)
    if not product:
        return jsonify({"error": "Not found"}), 404
    return jsonify(product.__dict__)


@app.route("/products", methods=['POST'])
def create():
    """
    Creates a new product based on the JSON data provided in the request body.
    Sends an email notification upon successful product creation.

    Request Body Example:
        {
            "name": "New Product",
            "qty": 100,
            "price": 29.99
        }

    Returns:
        jsonify: A JSON object of the newly created product with a 201 status,
                 or an error message with a 500 status if an exception occurs.
    """
    data = request.get_json()
    try:
        prod = repo.Product(name=data['name'], qty=data['qty'], price=data['price'])
        pid = repo.create_product(prod)
        saved = repo.read_product_by_id(pid)
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_gmail("owner@example.com", f"Product Created at {now_str}", f"{saved.__dict__}")
        return jsonify(saved.__dict__), 201
    except Exception as e:
        logging.error(f"Error creating product: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/products/<int:prod_id>", methods=['PUT'])
def update(prod_id):
    """
    Updates an existing product identified by `prod_id` with the
    JSON data provided in the request body.

    Args:
        prod_id (int): The ID of the product to update.

    Request Body Example:
        {
            "name": "Updated Product Name",
            "qty": 150,
            "price": 35.50
        }

    Returns:
        jsonify: A JSON object of the updated product.
    """
    data = request.get_json()
    prod = repo.Product(id=prod_id, name=data['name'], qty=data['qty'], price=data['price'])
    repo.update_product(prod)
    updated = repo.read_product_by_id(prod_id)
    return jsonify(updated.__dict__)


@app.route("/products/<int:prod_id>", methods=['DELETE'])
def delete(prod_id):
    """
    Deletes a product from the repository by its ID.

    Args:
        prod_id (int): The ID of the product to delete.

    Returns:
        jsonify: A JSON object indicating the status of the deletion.
    """
    repo.delete_product(prod_id)
    return jsonify({"status": "deleted"})


@app.route("/stock/total", methods=['GET'])
def total_stock():
    """
    Calculates and returns the total stock quantity of all products.

    Returns:
        jsonify: A JSON object containing the total stock quantity.
    """
    total = stock_calc.total_stock()
    return jsonify({"total_stock": total})


@app.route("/products/scrape", methods=['GET'])
def scrape_products():
    """
    Initiates a web scraping process to fetch product data.

    Returns:
        jsonify: A JSON object containing the scraped product data.
    """
    products = scraper.scrape_products()
    return jsonify(products)


if __name__ == "__main__":
    # Runs the Flask application in debug mode.
    # In a production environment, debug=False should be used,
    # and a production-ready WSGI server should be employed.
    app.run(debug=True)