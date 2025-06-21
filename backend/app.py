from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Flask backend running!'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name', '')

    if not name:
        return jsonify({'message': 'Name not provided!'}), 400

    print(f"Received name: {name}")
    return jsonify({'message': f'Hello, {name}! Your name was submitted successfully.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
