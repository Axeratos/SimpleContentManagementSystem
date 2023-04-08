from flask import Flask

from app.api.api_v1.api_register import api_router
from app.core.config import app_config


def create_app() -> Flask:
    flask_app = Flask(__name__)
    flask_app.secret_key = app_config.APP_SECRET_KEY
    flask_app.register_blueprint(api_router)
    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
