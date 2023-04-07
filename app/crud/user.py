from pydantic import EmailStr
from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from app import User
from app.crud import CRUDBase


class CRUDUser(CRUDBase):
    def __init__(self, session: Session):
        super().__init__(session=session, model=User)

    def get_by_phone_email(self, phone_nuber: str, login: EmailStr):
        return self.session.scalar(select(self.model).where(or_(User.phone_number == phone_nuber, User.login == login)))
