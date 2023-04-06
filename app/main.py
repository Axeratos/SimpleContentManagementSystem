from flask import Flask

app = Flask(__name__)


@app.get("/")
def main_route():
    return "Hello, I am working"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
