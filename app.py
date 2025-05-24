from flask import Flask, render_template, request, jsonify
from decoder import decode_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/decode", methods=["POST"])
def decode():
    content = request.get_json()
    try:
        result = decode_data(content["data"], content["protocol"])
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
