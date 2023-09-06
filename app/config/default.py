from os import environ

from pydantic_settings import BaseSettings


class DefaultSettings(BaseSettings):
    POSTGRES_DB: str = environ.get("POSTGRES_DB", "exif")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_USER: str = environ.get("POSTGRES_USER", "user")
    POSTGRES_PORT: int = int(environ.get("POSTGRES_PORT", "5432")[-4:])
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "12345")


def get_settings():
    return DefaultSettings()
