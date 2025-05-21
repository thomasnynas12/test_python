import redis.asyncio as redis
from app.domain.config import REDIS_HOST, REDIS_PORT

class RedisCache:
    def __init__(self):
        self.client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

    async def get(self, key):
        val = await self.client.get(key)
        return val.decode() if val else None

    async def set(self, key, value, ttl=3600):
        await self.client.set(key, value, ex=ttl)
