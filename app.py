from flask import Flask, request, jsonify

app = Flask(__name__)

def subtract(x, y):
    return x - y

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y    

@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/calc/<operation>/<int:x>/<int:y>")
def calc(operation, x, y):
    result = None

    if operation == "add":
        result = add(x, y)
    elif operation == "subtract":
        result = subtract(x, y)
    elif operation == "multiply":
        result = multiply(x, y)
    else:
        return jsonify({"error": "Invalid operation. Please use add, subtract, or multiply."})

    return jsonify({"result": result})

if __name__ == "__main__":
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

