from datetime import datetime

from sqlalchemy import String, Text, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Post(Base):
    __tablename__ = "posts"
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    user = relationship("User", back_populates="posts")
    user_id = mapped_column(ForeignKey("users.pk"))
