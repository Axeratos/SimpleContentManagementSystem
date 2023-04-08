from datetime import datetime

from pydantic import BaseModel, validator


class BasePostSchema(BaseModel):
    title: str | None
    content: str | None
    created_at: datetime | None

    @validator("title")
    def validate_title(cls, value):
        if value and len(value) > 100:
            raise ValueError("Title is too long")
        return value


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
