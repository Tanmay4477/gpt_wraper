from pydantic_settings import BaseSettings, SettingsConfigDict
import anthropic

class Settings(BaseSettings):
    api_key: str = 'api'
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

client = anthropic.Anthropic(
    api_key=settings.api_key
)


