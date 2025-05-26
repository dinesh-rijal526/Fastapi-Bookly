from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL : str 

    model_config = SettingsConfigDict(
        env_file= '.env',
        extra= 'ignore'
    )

Config = Settings(DATABASE_URL='postgresql+asyncpg://neondb_owner:npg_9aArvu4LUPiJ@ep-sparkling-mud-a82rsk8e-pooler.eastus2.azure.neon.tech/neondb?')