
import os
from dotenv import load_dotenv

from pathlib import Path
env_path  = Path('.') / '.env'
load_dotenv(dotenv_path= env_path)


class Settings:
    PROJECT_TITLE: str = "Boutique 👗"

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER','localhost')
    POSTGRES_PORT: int = os.getenv('POSTGRES_PORT',5433)
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
    SECRET_KEY = str = os.getenv("SECRET_KEY")
    ALGORITHM = str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = int = 30           #60 * 24 * 7  # 7 days

settings = Settings()