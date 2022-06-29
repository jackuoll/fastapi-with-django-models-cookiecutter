from pydantic import BaseSettings


class Settings(BaseSettings):
    db_name: str = "my_db"
    db_host: str = "localhost"
    db_user: str = "username"
    db_pass: str = "password"

    static_folder: str = "web/static"
    templates_folder: str = "web/templates"

    class Config:
        env_file = '.env'


SETTINGS = Settings()
