from pydantic import BaseModel, EmailStr


class BaseUserSchema(BaseModel):
    name: str | None
    phone_number: str | None
    login: EmailStr | None
    password: str | None


class UserCreate(BaseUserSchema):
    name: str
    phone_number: str
    login: EmailStr
    password: str


class UserUpdate(BaseUserSchema):
    pass


class UserLogin(BaseUserSchema):
    login: EmailStr
    password: str


class UserSchema(BaseUserSchema):
    name: str
    phone_number: str
    login: str

    class Config:
        orm_mode = True
