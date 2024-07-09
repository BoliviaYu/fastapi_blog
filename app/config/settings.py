from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application.
    """

    # FastAPI settings
    VESION: str = "0.1.0"
    APP_TITLE = "FastAPI-Blog"
    APP_DESCRIPTION = "A simple blog application built with FastAPI"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"

    # Database settings
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    # JWT settings
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
