from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import app_config

engine = create_engine(app_config.get_db_url(), echo=True)

Session = sessionmaker(bind=engine, expire_on_commit=False)
