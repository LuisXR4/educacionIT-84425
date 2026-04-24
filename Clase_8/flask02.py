from flask import jsonify, Flask

app = Flask(__name__)

@app.route("/api/status")
def get_status():
    resultado = {
        "estado": "activo",
        "version": "1.1.1",
        "servicios": ["NLP", "Vision Artificial", "ML"]
    }
    return jsonify(resultado), 200


if __name__ == "__main__":
    app.run(debug=True)