from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Add logic to store user details in the database
    if username and email and password:
        # For example, you can save the data to a SQLite database here.
        return jsonify({'message': 'User registered successfully'}), 200
    else:
        return jsonify({'error': 'Missing data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
