from flask import Blueprint, request, make_response

from app.core import hash_password
from app.crud import CRUDUser
from app.db import get_db_session
from app.schemas import UserCreate, UserSchema
from app.schemas.services.data_validation import validate, generate_user_exists_error

router = Blueprint("auth", __name__, url_prefix="/auth")


@router.post("/register")
@validate(body_model=UserCreate)
def register():
    user_data = request.get_json()
    db_session = get_db_session()
    user_crud = CRUDUser(db_session)
    if user_object := user_crud.get_by_phone_email(phone_nuber=user_data["phone_number"], login=user_data["login"]):
        error_message = generate_user_exists_error(
            user_object=user_object,
            phone=user_data["phone_number"],
            login=user_data["login"],
        )
        return make_response(error_message, 400)
    user_data["password"] = hash_password(user_data["password"])
    new_user = user_crud.create(create_data=user_data)
    return make_response(UserSchema.from_orm(new_user).json(), 201)


@router.post("/login")
def login():
    pass


@router.post("/logout")
def logout():
    pass
