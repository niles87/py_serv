from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return {
        "message": "App is awake"
    }


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
