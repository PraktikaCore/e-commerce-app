from flask import Flask, jsonify

app = Flask(__name__)

products_db = [
    {"id": 1, "name": "Laptop", "price": 350.25},
    {"id": 2, "name": "Smartphone", "price": 400.00},
    {"id": 3, "name": "Headphones", "price": 149.99}
]

@app.route('/list', methods=['GET'])
def list_products():
    """
    List all products
    ---
    tags:
      - Product Operations
    responses:
      200:
        description: A list of products
        schema:
          type: array
          items:
            $ref: '#/definitions/Product'
    """
    return jsonify(products_db)

@app.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Fetch a product given its identifier
    ---
    tags:
      - Product Operations
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: The product identifier
    responses:
      200:
        description: The requested product
        schema:
          $ref: '#/definitions/Product'
      404:
        description: Product not found
    definitions:
      Product:
        type: object
        properties:
          id:
            type: integer
            description: The product unique identifier
          name:
            type: string
            description: The product name
          price:
            type: number
            format: float
            description: The product price
    """
    product = next((p for p in products_db if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": f"Product {product_id} not found"}), 404

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)