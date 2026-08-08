from flask import Flask, jsonify, request
from flask_cors import CORS
from loadData import load_data, get_tables

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/tables")
def tables():
    try:
        return jsonify({"tables": get_tables()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/data")
def data():
    table = request.args.get("table")
    try:
        columns, rows = load_data(table)
        return jsonify({"columns": columns, "rows": [list(r) for r in rows]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5050)
