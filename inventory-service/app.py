from flask import Flask, jsonify

app = Flask(__name__)

stock_db = [
    {"id": 1, "stock": 50},
    {"id": 2, "stock": 200}
]

@app.route('/list', methods=['GET'])
def list_stock():
    """
    List inventory
    ---
    tags:
      - Inventory Operations
    responses:
      200:
        description: A list of stock levels
        schema:
          type: array
          items:
            $ref: '#/definitions/StockLevel'
    """
    return jsonify(stock_db)

@app.route('/<int:product_id>', methods=['GET'])
def get_stock_level(product_id):
    """
    Get the current stock level for a product
    ---
    tags:
      - Inventory Operations
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: The product identifier
    responses:
      200:
        description: The current stock level
        schema:
          $ref: '#/definitions/StockLevel'
    definitions:
      StockLevel:
        type: object
        properties:
          id:
            type: integer
            description: The product unique identifier
          stock:
            type: integer
            description: Available stock quantity
    """
    product = next((p for p in stock_db if p["id"] == product_id), None)
    quantity = product["stock"] if product else 0
    return jsonify({"product_id": product_id, "stock": quantity})

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)