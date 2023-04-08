from redis import Redis

from core.config import app_config

redis_db = Redis(app_config.REDIS_HOST, port=6379, decode_responses=True)
