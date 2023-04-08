from pydantic import BaseModel, EmailStr, validator


class BaseUserSchema(BaseModel):
    name: str | None
    phone_number: str | None
    login: EmailStr | None
    password: str | None

    @validator("phone_number")
    def validate_phone_number(cls, value):
        if value and len(value) > 15:
            raise ValueError("Phone number is too long. Max length is 15 characters")
        return value


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
