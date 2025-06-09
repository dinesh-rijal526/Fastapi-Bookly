from pydantic_settings import BaseSettings, SettingsConfigDict



# import os
# from dotenv import load_dotenv
# load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")
# JWT_SECRET = os.getenv("JWT_SECRET")
# JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
# REDIS_HOST = os.getenv("REDIS_HOST")
# REDIS_PORT = os.getenv("REDIS_PORT")


class Settings(BaseSettings):
    DATABASE_URL: str | None
    JWT_SECRET: str | None
    JWT_ALGORITHM: str | None
    REDIS_HOST: str  = "localhost"
    REDIS_PORT: int = 6379

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

Config = Settings(
    DATABASE_URL="postgresql+asyncpg://neondb_owner:npg_9aArvu4LUPiJ@ep-sparkling-mud-a82rsk8e-pooler.eastus2.azure.neon.tech/neondb?",
    JWT_SECRET="39520b09173dbbb87d06d645079ae50c",
    JWT_ALGORITHM="HS256",
    REDIS_HOST="localhost",
    REDIS_PORT=6379
)

