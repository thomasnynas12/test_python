# app/config.py
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = Field("postgresql+asyncpg://user:password@localhost/loan_db", env="DATABASE_URL")

    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: str = Field("localhost:9092", env="KAFKA_BOOTSTRAP_SERVERS")
    KAFKA_TOPIC: str = Field("loan_applications", env="KAFKA_TOPIC")
    KAFKA_GROUP_ID: str = Field("loan_group", env="KAFKA_GROUP_ID")

    # Redis
    REDIS_URL: str = Field("redis://localhost:6379", env="REDIS_URL")
    REDIS_CACHE_TTL: int = Field(3600, env="REDIS_CACHE_TTL")  # in seconds

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
