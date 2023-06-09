from flask import Blueprint, request, session, make_response

from crud import CRUDPost
from db import get_db_session
from schemas import PostCreate, PostSchema, PostUpdate
from schemas.query_schemas import PaginationQuerySchema
from schemas.services.data_validation import validate, get_user_id

router = Blueprint("post", __name__, url_prefix="/post")


@router.get("/")
@validate(query_model=PaginationQuerySchema)
def get_all_posts():
    pagination_params = PaginationQuerySchema(**request.args)
    db_session = get_db_session()
    crud_post = CRUDPost(session=db_session)
    queryset = crud_post.get_paginated(**pagination_params.dict())
    return [PostSchema.from_orm(post_object).dict() for post_object in queryset]


@router.post("/")
@validate(body_model=PostCreate)
def create_post():
    access_token = session.get("jwt")
    user_id, response = get_user_id(access_token=access_token)
    if response:
        return response
    post_data_validated = PostCreate(**request.get_json())
    db_session = get_db_session()
    crud_post = CRUDPost(session=db_session)
    post_data = {**post_data_validated.dict(), "user_id": user_id}
    new_post = crud_post.create(post_data)
    return make_response(PostSchema.from_orm(new_post).dict(), 201)


@router.get("/<int:post_id>")
def get_post(post_id):
    db_session = get_db_session()
    crud_post = CRUDPost(session=db_session)
    post_object = crud_post.get(pk=post_id)
    if not post_object:
        return make_response({"msg": "Post does not exist"}, 404)
    return PostSchema.from_orm(post_object).dict()


@router.put("/<int:post_id>")
@validate(body_model=PostUpdate)
def update_post(post_id):
    access_token = session.get("jwt")
    user_id, response = get_user_id(access_token=access_token)
    if response:
        return response
    db_session = get_db_session()
    crud_post = CRUDPost(session=db_session)
    old_object = crud_post.get(pk=post_id, user_id=user_id)
    if not old_object:
        return make_response({"msg": "Post does not exist"}, 404)
    update_data_validated = PostUpdate(**request.get_json())
    updated_object = crud_post.update(old_object, update_data_validated.dict(exclude_unset=True))
    return PostSchema.from_orm(updated_object).dict()


@router.delete("/<int:post_id>")
def delete_post(post_id):
    access_token = session.get("jwt")
    user_id, response = get_user_id(access_token=access_token)
    if response:
        return response
    db_session = get_db_session()
    crud_post = CRUDPost(session=db_session)
    deleted_object = crud_post.delete(pk=post_id, user_id=user_id)
    if not deleted_object:
        return make_response({"msg": "Post does not exist"}, 404)
    return PostSchema.from_orm(deleted_object).dict()
