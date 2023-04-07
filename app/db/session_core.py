from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import app_config

engine = create_engine(app_config.get_db_url(), echo=True)

Session = sessionmaker(bind=engine, expire_on_commit=False)


def get_db_session():
    with Session() as session:
        with session.begin():
            return session
