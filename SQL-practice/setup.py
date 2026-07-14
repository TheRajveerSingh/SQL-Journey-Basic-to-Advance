# setup.py
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

load_dotenv()
password = os.getenv("DB_PASSWORD")
engine = create_engine(f"mysql+mysqldb://root:{password}@localhost/practicedel")