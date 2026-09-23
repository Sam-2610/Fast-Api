from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time

SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:2610@localhost/new'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind= engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

""" while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="new",
            user="postgres",
            password="2610",
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database Connection was Sucessful!")
        break
    except Exception as error:
        print("Connection Failed", error)
        time.sleep(2) """