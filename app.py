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

if __name__ == '__main__':
    app.run()
