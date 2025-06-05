from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


Config = Settings(DATABASE_URL="postgresql+asyncpg://neondb_owner:npg_9aArvu4LUPiJ@ep-sparkling-mud-a82rsk8e-pooler.eastus2.azure.neon.tech/neondb?",
                  JWT_SECRET="39520b09173dbbb87d06d645079ae50c",
                  JWT_ALGORITHM="HS256"
)
