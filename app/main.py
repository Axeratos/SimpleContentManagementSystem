from flask import Flask, request, session

from app.api.api_v1.api_register import api_router
from app.core.config import app_config

app = Flask(__name__)
app.secret_key = app_config.APP_SECRET_KEY

app.register_blueprint(api_router)


@app.get("/")
def main_route():
    return {"msg": "Hello, I am working"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
