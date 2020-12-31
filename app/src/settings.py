from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Github stat API"
    GITHUB_BASE_URL: str = "https://api.github.com"

    class Config:
        env_file = "../.env"


@lru_cache()
def settings():
    return Settings()