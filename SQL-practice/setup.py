# setup.py
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Always resolve .env relative to this setup.py file, not the caller's cwd
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

password = os.getenv("DB_PASSWORD")
engine = create_engine(f"mysql+mysqldb://root:{password}@localhost/practicedel")