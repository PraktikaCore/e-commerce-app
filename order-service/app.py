from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/create', methods=['POST'])
def create_order():
    """
    Create a new order
    ---
    tags:
      - Order Operations
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: OrderRequest
          required:
            - product_id
          properties:
            product_id:
              type: integer
              description: ID of the product to order
            quantity:
              type: integer
              description: Quantity to order
              default: 1
    responses:
      201:
        description: Order created successfully
        schema:
          id: OrderResponse
          properties:
            message:
              type: string
              description: Status message
            product:
              $ref: '#/definitions/ProductInfo'
      404:
        description: Product not found
      500:
        description: Internal Server Error
    definitions:
      ProductInfo:
        type: object
        properties:
          id:
            type: integer
          name:
            type: string
          price:
            type: number
            format: float
    """
    data = request.get_json()
    product_id = data.get('product_id')

    try:
        product_response = requests.get(f"http://product-service/{product_id}")
        product_response.raise_for_status()
        product_data = product_response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return jsonify({"error": f"Product ID {product_id} not found in Product Service."}), 404
        else:
            return jsonify({"error": f"Error from Product Service: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Could not connect to Product Service: {e}"}), 500

    return jsonify({
        'message': 'Order created',
        'product': product_data
    }), 201

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)