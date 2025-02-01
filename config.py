from pydantic_settings import BaseSettings, SettingsConfigDict
import anthropic

class Settings(BaseSettings):
    api_key:str
    model_config = SettingsConfigDict(env_file=".env", env_prefix="MYAPP_")

settings = Settings()

client = anthropic.Anthropic(
    api_key=settings.api_key
)


