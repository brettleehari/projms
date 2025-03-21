from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "My Microservice"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
