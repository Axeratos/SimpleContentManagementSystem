from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    login: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    posts = relationship("Post", back_populates="user")
