from sqlalchemy import select, asc, desc
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Post


class CRUDPost(CRUDBase):
    def __init__(self, session: Session):
        super().__init__(session=session, model=Post)

    def get_paginated(self, limit: int, offset: int, ordering: str):
        orderings = {"asc": asc, "desc": desc}
        return self.session.scalars(
            select(self.model).order_by(orderings[ordering](Post.created_at)).limit(limit).offset(offset)
        )
