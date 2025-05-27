from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DB_CONNECTION = "sqlite:///./blog.db"

engine = create_engine(SQL_DB_CONNECTION,connect_args={"check_same_thread":False})

sessinlocal = sessionmaker(bind=engine,autoflush=False, autocommit = False)

Base = declarative_base()

def get_db():
    db = sessinlocal()
    try:
        yield db
    finally:
        db.close()