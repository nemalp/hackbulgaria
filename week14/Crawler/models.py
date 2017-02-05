from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from settings import DB_NAME

engine = create_engine(DB_NAME)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Server(Base):
    __tablename__ = 'servers'

    name = Column(String, primary_key=True)
    number = Column(Integer)

Base.metadata.create_all(engine)
