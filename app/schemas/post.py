from datetime import datetime

from pydantic import BaseModel


class BasePostSchema(BaseModel):
    title: str | None
    content: str | None
    created_at: datetime | None


class PostCreate(BasePostSchema):
    title: str
    content: str


class PostUpdate(BasePostSchema):
    pass


class PostSchema(BasePostSchema):
    pk: int
    title: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True
