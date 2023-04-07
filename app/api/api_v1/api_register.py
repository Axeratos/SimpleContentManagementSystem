from flask import Blueprint

from .endpoints import auth, posts

api_router = Blueprint("v1", __name__, url_prefix="/v1")

api_router.register_blueprint(auth.router)
api_router.register_blueprint(posts.router)
