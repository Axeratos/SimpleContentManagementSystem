from flask import Flask

from app.api.api_v1.api_register import api_router

app = Flask(__name__)

app.register_blueprint(api_router)


@app.get("/")
def main_route():
    return {"msg": "Hello, I am working"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
