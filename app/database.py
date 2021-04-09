from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from os import getenv
from sqlalchemy.ext.declarative import DeclarativeMeta
import json

def get_db_url():
    return "postgresql://{}:{}@{}/{}".format(
        getenv('POSTGRES_USER'),
        getenv('POSTGRES_PASSWORD'),
        getenv('POSTGRES_HOST'),
        getenv('POSTGRES_DB')
    )


SQLALCHEMY_DATABASE_URL = get_db_url()

# TODO: Use TLS to connect
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()