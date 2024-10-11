from flask import Blueprint, request, jsonify
from controllers.product_controller import get_products
# from ..models import Product
# from ..extensions import db

product_blueprint = Blueprint('product', __name__)

@product_blueprint.route('/getproducts', methods=['GET'])
def get_products_route():
    return get_products()