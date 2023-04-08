from typing import Type

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import Base


class CRUDBase:
    def __init__(self, session: Session, model: Type[Base]):
        self.session = session
        self.model = model

    def get(self, **kwargs):
        return self.session.scalar(select(self.model).filter_by(**kwargs))

    def get_all(self):
        return self.session.scalars(select(self.model)).all()

    def create(self, create_data: dict):
        model_object = self.model(**create_data)
        self.session.add(model_object)
        self.session.flush()
        self.session.refresh(model_object)
        self.session.commit()
        return model_object

    def update(self, old_object: Type[Base], update_data: dict):
        for key in update_data:
            setattr(old_object, key, update_data[key])
        self.session.flush()
        return old_object

    def delete(self, **kwargs):
        db_object = self.get(**kwargs)
        if not db_object:
            return
        self.session.delete(db_object)
        return db_object
