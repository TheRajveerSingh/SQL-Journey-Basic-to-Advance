1. Activate the virtual enviroment in the terminal first: sql-env\Scripts\activate
2. Whenever opening a new Jupyter file:
-> Start the kernal: sql-env
-> First cell:
%load_ext sql
%run setup.py
%sql engine
3. For now, the database being used in 'practicedel'. We can either change the name whenever needed, or just create a new setup for another database. However, if only a dabase needs to be used only once or twice, write the first cell in the jupyter file as:
%load_ext sql
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
password = os.getenv("DB_PASSWORD")
print(password)  # sanity check - make sure this isn't None

engine = create_engine(f"mysql+mysqldb://root:{password}@localhost/practicedel")
%sql engine