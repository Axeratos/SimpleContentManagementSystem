from datetime import timedelta

from flask import Blueprint, request, make_response, session

from app.core import hash_password, verify_password
from app.core.security import create_token
from app.crud import CRUDUser
from app.db import get_db_session
from app.db.redis_connection import redis_db
from app.schemas import UserCreate, UserSchema, UserLogin
from app.schemas.services.data_validation import validate, generate_user_exists_error

router = Blueprint("auth", __name__, url_prefix="/auth")


@router.post("/register")
@validate(body_model=UserCreate)
def register():
    user_data = request.get_json()
    db_session = get_db_session()
    user_crud = CRUDUser(session=db_session)
    if user_object := user_crud.get_by_phone_email(phone_nuber=user_data["phone_number"], login=user_data["login"]):
        error_message = generate_user_exists_error(
            user_object=user_object,
            phone=user_data["phone_number"],
            login=user_data["login"],
        )
        return make_response(error_message, 400)
    user_data["password"] = hash_password(user_data["password"])
    user_data_validated = UserCreate(**user_data)
    new_user = user_crud.create(create_data=user_data_validated.dict())
    return make_response(UserSchema.from_orm(new_user).dict(exclude={"password"}), 201)


@router.post("/login")
@validate(body_model=UserLogin)
def login():
    login_data = request.get_json()
    db_session = get_db_session()
    user_crud = CRUDUser(session=db_session)
    user_object = user_crud.get(login=login_data["login"])
    if not user_object:
        return make_response({"field": "login", "msg": "User does not exist"}, 404)
    elif not verify_password(login_data["password"], user_object.password):
        return make_response({"field": "password", "msg": "Password is incorrect"}, 400)

    access_token = create_token()
    redis_db.set(access_token, user_object.pk, ex=timedelta(days=1))

    session["jwt"] = access_token
    return access_token


@router.post("/logout")
def logout():
    if "jwt" in session:
        access_token = session.pop("jwt")
        redis_db.delete(access_token)
    else:
        redis_db.delete(request.get_json()["jwt"])
    return {"msg": "User logged out successfully"}
