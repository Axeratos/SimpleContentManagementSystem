from functools import wraps
from typing import Type, Callable
from flask import request, make_response

from pydantic import BaseModel, ValidationError, EmailStr

from app import User


def validate(
    body_model: Type[BaseModel] | None = None,
    query_model: Type[BaseModel] | None = None,
):
    def decorate(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            errors = {}
            if query_model:
                query_params = request.args
                try:
                    query_model(**query_params.to_dict())
                except ValidationError as e:
                    errors["query"] = e.errors()
            if body_model:
                request_body = request.get_json()
                try:
                    body_model(**request_body)
                except TypeError:
                    content_type = request.headers.get("Content-Type", "").lower()
                    media_type = content_type.split(";")[0]
                    if media_type != "application/json":
                        error_body = {"detail": f"Unsupported media type '{media_type}'. application/json is required"}
                        return make_response(error_body, 415)
                    return make_response({"detail": "Could not parse json"}, 422)
                except ValidationError as e:
                    errors["body"] = e.errors()
            if errors:
                return make_response({"errors": errors}, 400)
            return func(*args, **kwargs)

        return wrapper

    return decorate


def generate_user_exists_error(user_object: User, phone: str, login: EmailStr) -> dict:
    error_schema = {"detail": {"loc": [], "msg": "User with this %s already exists"}}

    if user_object.phone_number == phone:
        error_schema["detail"]["loc"] = ["phone_number"]
        error_schema["detail"]["msg"] %= "phone number"
    elif user_object.login == login:
        error_schema["detail"]["loc"] = ["login"]
        error_schema["detail"]["msg"] %= "login"

    return error_schema
