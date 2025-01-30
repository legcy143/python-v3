from flask import Flask , jsonify

app = Flask(__name__)


@app.route('/')
def greet():
    try:
        return jsonify({"message": "good morning ok v2"})
    except Exception as e:
        return ({"message": "error"})


@app.route("/health")
def HelathCheck():
    return jsonify({"message": "Health is ok"})

if __name__ == "__main__":
    app.run(debug=True)
