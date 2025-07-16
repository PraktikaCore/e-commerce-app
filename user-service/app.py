from flask import Flask, jsonify

app = Flask(__name__)

# In-memory data store
users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route('/list', methods=['GET'])
def list_users():
    """
    List all users
    ---
    tags:
      - User Operations
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            $ref: '#/definitions/User'
    """
    return jsonify(users_db)

@app.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Fetch a user given their identifier
    ---
    tags:
      - User Operations
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The user identifier
    responses:
      200:
        description: The requested user
        schema:
          $ref: '#/definitions/User'
      404:
        description: User not found
    definitions:
      User:
        type: object
        properties:
          id:
            type: integer
            description: The user unique identifier
          name:
            type: string
            description: The user name
          email:
            type: string
            description: The user email
    """
    user = next((user for user in users_db if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": f"User {user_id} not found"}), 404

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)