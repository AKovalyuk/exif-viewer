from os import environ

from pydantic_settings import BaseSettings


class DefaultSettings(BaseSettings):
    POSTGRES_DB: str = environ.get("POSTGRES_DB", "exif")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_USER: str = environ.get("POSTGRES_USER", "user")
    POSTGRES_PORT: int = int(environ.get("POSTGRES_PORT", "5432")[-4:])
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "12345")
    REDIS_PORT: int = int(environ.get('REDIS_PORT', '6379'))
    REDIS_HOST: str = environ.get('REDIS_HOST', 'localhost')
    REDIS_DB: int = int(environ.get('REDIS_DB', '0'))
    UPLOAD_DIR: str = 'uploads/'

    def database_uri(self):
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}'\
               f'@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'

    def database_uri_sync(self):
        return f'postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}'\
               f'@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'

    def redis_uri(self):
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}'


def get_settings():
    return DefaultSettings()
