from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello World!"

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    return jsonify({"message": f"Hello {data['name']}! Data received successfully."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
