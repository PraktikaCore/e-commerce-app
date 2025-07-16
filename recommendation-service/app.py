from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/for-user/<string:user_id>', methods=['GET'])
def get_recommendations(user_id):
    """
    Get recommendations for a specific user
    ---
    tags:
      - Recommendation Operations
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: The user identifier
    responses:
      200:
        description: A list of recommendations for the user
        schema:
          id: Recommendation
          properties:
            user_id:
              type: string
              description: The user identifier
            recommendations:
              type: array
              items:
                type: string
              description: List of recommended product IDs
    """
    # Dummy recommendations
    return jsonify({"user_id": user_id, "recommendations": ["1", "2"]})

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)