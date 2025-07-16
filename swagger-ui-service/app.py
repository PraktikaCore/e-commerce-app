from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "E-commerce Microservices API",
        "description": "API documentation for all e-commerce microservices.",
        "version": "1.0.0"
    },
    "host": "mariia.local",  # This should be your ingress host
    "basePath": "/",
    "schemes": [
        "http"
    ],
    "paths": {
        "/product/list": {
            "get": {
                "summary": "Get all products",
                "tags": ["Product"],
                "produces": ["application/json"],
                "responses": {
                    "200": {
                        "description": "A list of products."
                    }
                }
            }
        },
        "/product/{product_id}": {
            "get": {
                "summary": "Get a specific product",
                "tags": ["Product"],
                "produces": ["application/json"],
                "parameters": [
                    {
                        "name": "product_id",
                        "in": "path",
                        "required": True,
                        "type": "integer"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Product details."
                    },
                    "404": {
                        "description": "Product not found."
                    }
                }
            }
        },
        "/order/create": {
            "post": {
                "summary": "Create an order",
                "tags": ["Order"],
                "produces": ["application/json"],
                "consumes": ["application/json"],
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "product_id": {
                                    "type": "integer"
                                },
                                "quantity": {
                                    "type": "integer"
                                }
                            }
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Order created."
                    },
                    "400": {
                        "description": "Invalid input."
                    }
                }
            }
        },
        "/user/list": {
            "get": {
                "summary": "Get all users",
                "tags": ["User"],
                "produces": ["application/json"],
                "responses": {
                    "200": {
                        "description": "A list of users."
                    }
                }
            }
        },
        "/user/{user_id}": {
            "get": {
                "summary": "Get a specific user",
                "tags": ["User"],
                "produces": ["application/json"],
                "parameters": [
                    {
                        "name": "user_id",
                        "in": "path",
                        "required": True,
                        "type": "integer"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "User details."
                    },
                    "404": {
                        "description": "User not found."
                    }
                }
            }
        },
        "/inventory/list": {
            "get": {
                "summary": "List all inventory",
                "tags": ["Inventory"],
                "produces": ["application/json"],
                "responses": {
                    "200": {
                        "description": "A list of inventory stock."
                    }
                }
            }
        },
        "/inventory/{product_id}": {
            "get": {
                "summary": "Get stock for a product",
                "tags": ["Inventory"],
                "produces": ["application/json"],
                "parameters": [
                    {
                        "name": "product_id",
                        "in": "path",
                        "required": True,
                        "type": "integer"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Stock details."
                    }
                }
            }
        },
        "/recommendation/for-user/{user_id}": {
            "get": {
                "summary": "Get recommendations for a user",
                "tags": ["Recommendation"],
                "produces": ["application/json"],
                "parameters": [
                    {
                        "name": "user_id",
                        "in": "path",
                        "required": True,
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "List of recommendations."
                    }
                }
            }
        }
    }
}

swagger_config = {
    "static_url_path": "/flasgger_static",  
    "url_prefix": "/swagger"
}

swagger = Swagger(app, template=swagger_template, config=swagger_config, merge=True)

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006)