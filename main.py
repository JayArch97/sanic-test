import os

from flask import Flask

app = Flask(__name__)


@app.route("/hello", methods=['GET', 'POST'])
def recieved_data():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the request body
        if data:
            title = data.get('title', 'No Title')
            body = data.get('body', 'No Body')
            id_value = data.get('id')
            response_message = f"Data received (POST): Title - {title}, Body - {body}, ID - {id_value}"
            return jsonify({"message": response_message, "received_data": data}), 200
        else:
            return jsonify({"error": "No JSON data received in the request body"}), 400
    else:  # Handle GET requests
        return "Hello from the GET request!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))