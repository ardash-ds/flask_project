from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .model import BaseModel

engine = create_engine('sqlite:///sqlite.db', echo=True)

BaseModel.metadata.create_all(engine)

Session = Session(bind=engine)

def get_sessionmaker(echo: bool):
    return sessionmaker(
        bind=engine(echo=echo),
        class_=Session,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )

def get_session():
    with get_sessionmaker() as session:
        yield session