from app.config import settings
import redis.asyncio as redis

class RedisCache:
    def __init__(self):
        self.client = redis.Redis(settings.REDIS_URL)

    async def get(self, key):
        val = await self.client.get(key)
        return val.decode() if val else None

    async def set(self, key, value, ttl=3600):
        await self.client.set(key, value, ex=ttl)