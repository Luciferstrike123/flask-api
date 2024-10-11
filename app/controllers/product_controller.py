from flask import request, jsonify
from models import Product

def get_products():
    try:
        products = Product.query.all()
        products_list = [
            {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price
            } for product in products
        ]

        return jsonify({"status": "success", "products": products_list}), 200
    except Exception as e:
        return jsonify({"status": "fail", "message": "No products found.", "error": str(e)}), 404