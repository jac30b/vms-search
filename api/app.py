from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/load', methods=['POST'])
def load_files():
    body = request.json
    return jsonify(body)