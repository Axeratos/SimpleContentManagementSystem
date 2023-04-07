from pydantic import BaseSettings
from pathlib import Path

env_path = Path(__file__).resolve().parents[2].joinpath(".env")
print(env_path)


class Config(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    PGPORT: int
    POSTGRES_DB: str

    REDIS_HOST: str

    JWT_SECRET_KEY: str

    def get_db_url(self):
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.PGPORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = env_path


app_config = Config()
print(app_config.get_db_url())
