from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

connect_args = {}
if settings.database_hostname not in ("localhost", "127.0.0.1:8000"):
    connect_args["sslmode"] = "require"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn= psycopg2.connect(host='localhost' , database='fastapi' , user='postgres', password='Cket@128', cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print('Database Conected Successfully')
#         break

#     except Exception as e:
#         print('Database Connection Failed')
#         print("ERROR: ", e)
#         time.sleep(2)
